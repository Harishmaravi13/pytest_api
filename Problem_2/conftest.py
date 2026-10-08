import pytest

@pytest.fixture
def cli_output():
    return """
Interface    Status    Protocol
Gi0/1        up        up
Gi0/2        up        up
Gi0/3        down      down
Gi0/4        up        up
"""