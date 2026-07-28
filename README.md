# Terminal-Native LLM Agent

A powerful, context-aware AI assistant that lives directly in your terminal. Powered by `google.antigravity`, this agent translates natural language into exact terminal commands and executes them for you safely.

## ✨ Features

- **Natural Language to Command**: Just tell the agent what you want to do, and it will generate the exact terminal command for your OS.
- **Safe Execution**: Built-in safety confirmation (`Execute this command? (y/n)`) before running any generated command.
- **Context-Aware**: The output of executed commands is fed back into the LLM, allowing it to understand the results of its actions and plan the next steps.
- **Anti-Context Drift Checkpoints**: Automatically checks in every 5 turns to ensure it is still on the right track. If it starts hallucinating, you can provide feedback to instantly course-correct it without losing your entire conversation history.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- An API key for the LLM (configured via `.env`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SujAnverse1125/Terminal-native-LLM-Ag.git
   cd Terminal-native-LLM-Ag
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install python-dotenv google-antigravity
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory and add your required API keys:
   ```env
   # Example
   API_KEY=your_api_key_here
   ```

### Usage

Run the agent script:
```bash
python agent.py
```

- Type your request (e.g., `"list all python files in this directory"`).
- The agent will generate the command.
- Press `y` to execute it or `n` to skip.
- Type `quit`, `exit`, or `bye` to stop the agent.

## 🛡️ Security Note
The `.env` file and `venv` directory are included in the `.gitignore` to prevent sensitive API keys from being accidentally uploaded to GitHub.

## 🔮 Future Plans / Roadmap
- **Local LLM Support**: Integration with tools like Ollama to run models locally for completely free, offline usage.
- **Advanced RAG Integration**: Adding Retrieval-Augmented Generation to allow the agent to understand and search through entire codebases.
- **Multi-Agent Collaboration**: Allowing multiple specialized agents to work together on complex terminal workflows.
- **Cross-Platform Enhancements**: Further optimizations for seamless execution across Windows, macOS, and Linux environments.