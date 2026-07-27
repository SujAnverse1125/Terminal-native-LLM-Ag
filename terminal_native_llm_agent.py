"""Terminal-native LLM agent powered by Google Antigravity."""

from __future__ import annotations

import importlib
from dataclasses import dataclass


DEFAULT_ANTIGRAVITY_MODULE = "google_antigravity"
DEFAULT_GEMINI_MODEL = "gemini-2.5-pro"


@dataclass(frozen=True)
class AgentConfig:
    model: str = DEFAULT_GEMINI_MODEL
    session_store_path: str = ".antigravity_state"


def _load_antigravity(module_name: str = DEFAULT_ANTIGRAVITY_MODULE):
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Google Antigravity SDK is not installed. "
            "Install the SDK and try again."
        ) from exc


def start_terminal_agent(
    config: AgentConfig | None = None, module_name: str = DEFAULT_ANTIGRAVITY_MODULE
) -> None:
    """Start the terminal-native agent using Antigravity's managed loop."""
    active_config = config or AgentConfig()
    antigravity = _load_antigravity(module_name=module_name)
    workforce = antigravity.WorkforceManager(
        model=active_config.model,
        state_path=active_config.session_store_path,
    )
    workforce.run_terminal()


if __name__ == "__main__":
    start_terminal_agent()
