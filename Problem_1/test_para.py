import pytest
from para import validation
validate = validation()

devices = [
    ("R1", "192.168.257.1", "UP",False),
    ("R2", "192.168.1.2", "DOWN",True),
    ("SW1", "192.168.1.F", "UP",False),
    ("SW2", "192.168.1.4", "UP",True)
    ]

@pytest.mark.parametrize(
    "hostname, ip, status,expected", devices)
def test_verify(hostname,ip,status,expected):
    result = validate.verify(hostname,ip,status)
    print(f"{hostname} -> {'PASS' if result else 'FAIL'}")
    assert result == expected