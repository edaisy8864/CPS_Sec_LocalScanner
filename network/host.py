from typing import List

class Host:
    def __init__(self):
        self.ports: List[Port] = []
        self.mac_address = None
        self.ip_address = None


class Port:
    def __init__(self, port_id, service, protocol):
        self.port_id = port_id
        self.service = service
        self.protocol = protocol


    def __repr__(self):
        return "[Port {}/{} {}]".format(self.port_id, self.protocol, self.service)

    def __str__(self):
        return self.__repr__()