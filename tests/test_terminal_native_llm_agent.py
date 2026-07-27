import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from terminal_native_llm_agent import AgentConfig, start_terminal_agent


class TerminalNativeLLMAgentTests(unittest.TestCase):
    def test_starts_antigravity_workforce_manager(self):
        run_terminal = Mock()
        workforce_manager = Mock(return_value=SimpleNamespace(run_terminal=run_terminal))
        fake_sdk = SimpleNamespace(WorkforceManager=workforce_manager)

        with patch("terminal_native_llm_agent.importlib.import_module", return_value=fake_sdk):
            start_terminal_agent(AgentConfig(model="gemini-test", session_store_path="/tmp/state"))

        workforce_manager.assert_called_once_with(model="gemini-test", state_path="/tmp/state")
        run_terminal.assert_called_once_with()

    def test_raises_clear_error_when_sdk_missing(self):
        with patch(
            "terminal_native_llm_agent.importlib.import_module",
            side_effect=ModuleNotFoundError("missing"),
        ):
            with self.assertRaisesRegex(RuntimeError, "Google Antigravity SDK is not installed"):
                start_terminal_agent()


if __name__ == "__main__":
    unittest.main()
