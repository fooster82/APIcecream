import pytest
import app
from controllers import icecreams

@pytest.fixture
def api(monkeypatch):
    test_facts = [
        {'id': 1, 'fact': 'Test Fact 1'},
        {'id': 2, 'fact': 'Test Fact 2'}
    ]
    monkeypatch.setattr(icecreams, "facts", test_facts)
    api = app.app.test_client()
    return api