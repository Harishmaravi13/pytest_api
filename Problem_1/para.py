import ipaddress 
class validation:
    def __init__(self):
        pass

    def verify(hostname,ip,status):
        valid_hostname = hostname.startswith(("R","SW"))
        try:
            ipaddress.ip_address(ip)
            ip_valid=True
        except ValueError:
            ip_valid =False
        valid_status = status in ["UP","DOWN"]

        return valid_hostname and ip_valid and valid_status

