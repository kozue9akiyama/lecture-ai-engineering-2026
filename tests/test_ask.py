from types import SimpleNamespace
from unittest.mock import call, Mock

import app.ask as ask_module
from app.config import MODEL


def test_main_reuses_chat_for_followup_questions(monkeypatch):
    chat = Mock()
    chat.send_message.side_effect = [
        SimpleNamespace(text="first answer", usage_metadata=None),
        SimpleNamespace(text="second answer", usage_metadata=None),
    ]
    client = Mock()
    client.chats.create.return_value = chat

    monkeypatch.setattr(ask_module.genai, "Client", lambda api_key: client)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")
    monkeypatch.setattr("sys.argv", ["app.ask", "first question"])
    questions = iter(["follow-up question", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(questions))

    ask_module.main()

    client.chats.create.assert_called_once_with(model=MODEL)
    assert chat.send_message.call_args_list == [
        call("first question"),
        call("follow-up question"),
    ]