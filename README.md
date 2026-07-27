# Terminal-native-LLM-Ag

This repository now uses the **Google Antigravity SDK** as the agent runtime layer.
Instead of implementing a custom terminal while-loop, the CLI delegates lifecycle,
state, and terminal orchestration to Antigravity's managed `WorkforceManager`.

## Run

1. Install the Google Antigravity SDK in your environment.
2. Start the terminal-native agent:

```bash
python /home/runner/work/Terminal-native-LLM-Ag/Terminal-native-LLM-Ag/terminal_native_llm_agent.py
```

By default, the session state is stored under `.antigravity_state`.

## Test

```bash
cd /home/runner/work/Terminal-native-LLM-Ag/Terminal-native-LLM-Ag
python -m unittest discover -s tests -p "test_*.py"
```