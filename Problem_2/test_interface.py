import re

class InterfaceParser:

    def __init__(self, cli_output):
        self.cli_output = cli_output

    def get_interfaces(self):
        pattern = r"(Gi\d+/\d+)\s+(up|down)\s+(up|down)"
        return re.findall(pattern, self.cli_output)

    def get_interface_states(self):
        actual = {}

        for interface, status, protocol in self.get_interfaces():
            actual[interface] = status

        return actual


expected = {
    "Gi0/1": "up",
    "Gi0/2": "up",
    "Gi0/3": "down",
    "Gi0/4": "up"
}


class TestInterfaces:

    def test_all_interfaces(self, cli_output):

        parser = InterfaceParser(cli_output)

        for interface, status, protocol in parser.get_interfaces():
            assert status == "up", f"{interface} is DOWN"

    def test_interface_states(self, cli_output):

        parser = InterfaceParser(cli_output)

        actual = parser.get_interface_states()

        assert actual == expected