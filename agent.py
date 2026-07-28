from dotenv import load_dotenv
load_dotenv()
import asyncio
import sys
import subprocess
from google.antigravity import Agent, LocalAgentConfig

async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "You are a terminal execution assistant. When the user asks you to perform a task, "
            "reply ONLY with the exact, valid terminal command required to achieve it. "
            "Do not include markdown formatting, backticks, or conversational text."
        )
    )
    
    async with Agent(config) as agent:
        print("Antigravity Terminal Agent Started. Type 'quit' to exit.")
        turn_counter = 0
        CHECKPOINT_INTERVAL = 5
        last_output = ""
        
        while True:
            if turn_counter > 0 and turn_counter % CHECKPOINT_INTERVAL == 0:
                print("\n[System Checkpoint]: We've had a few exchanges.")
                on_track = input("Am I still on the right track to achieve your goal? (y/n): ")
                if on_track.lower() in ['n', 'no']:
                    feedback = input("[System]: Where did I go wrong?\nUser Feedback> ")
                    correction_prompt = (
                        f"SYSTEM OVERRIDE: User says you went off track. "
                        f"Feedback: '{feedback}'. "
                        f"Discard hallucinated context and return to original instructions."
                    )
                    try:
                        response = await agent.chat(correction_prompt)
                        async for token in response:
                            sys.stdout.write(token)
                            sys.stdout.flush()
                        print("\n")
                    except Exception as e:
                        print(f"\n[Error]: {e}")
                else:
                    print("[System]: Great! Continuing...")

            user_input = input("\nUser> ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                break
            
            if last_output:
                prompt = (
                    f"Last command output was:\n{last_output}\n\n"
                    f"User's next request: {user_input}"
                )
            else:
                prompt = user_input

            try:
                response = await agent.chat(prompt)
                
                command = ""
                print("\n[Generated Command]: ", end="")
                async for token in response:
                    sys.stdout.write(token)
                    sys.stdout.flush()
                    command += token
                print("\n")

                command = command.strip()

                confirm = input(f"Execute this command? (y/n): ")
                if confirm.lower() == 'y':
                    print("\n[Executing...]\n")
                    result = subprocess.run(
                        command,
                        shell=True,
                        capture_output=True,
                        text=True
                    )
                    output = result.stdout + result.stderr
                    last_output = output[:2000]
                    print(output)
                else:
                    last_output = ""

                turn_counter += 1
                
            except Exception as e:
                print(f"\n[Error]: {e}")

if __name__ == "__main__":
    asyncio.run(main())