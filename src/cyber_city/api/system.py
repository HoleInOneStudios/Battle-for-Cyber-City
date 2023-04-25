"""
The class for objects that communicate with the modbus server. It conects to the
server and can read and write.
"""

from pymodbus.client import ModbusTcpClient as ModbusClient

class System():
    """ The System class """
    def __init__(self, coil: int,
                host: str = '127.0.0.1', port: int = 502) -> None:
        self.__host: str = host
        """ IP address of the ModBus server """
        self.__port: int = port
        """ Port of the ModBus server """
        self.client = ModbusClient(self.__host, self.__port)
        """ Client used to connect to the ModBus server """
        self.coil: int = coil
        """ The coil address of the system on the ModBus server """
        self.state: bool = False
        """ The state of the system """

    @property
    def host(self) -> str:
        """ Getters and Setters for the modbus servers 'ip address' """
        return self.__host
    @host.setter
    def host(self, val: str) -> None:
        self.__host = val
        self.client = ModbusClient(self.__host, self.__port)

    @property
    def port(self) -> int:
        """ Getters and Setters for the modbus servers `port` """
        return self.__port
    @port.setter
    def port(self, val) -> None:
        self.__port = val
        self.client = ModbusClient(self.__host, self.__port)

    def enabled(self) -> None:
        """ Turn on the system by setting `state` to `True` """
        self.state = True
    def disable(self) -> None:
        """ Turn off the system by setting `state` to `False` """
        self.state = False
    def set(self, val: bool) -> None:
        """ 
        Set the system state by setting `state` to
        
        Arg:
            val (bool): new state
        """
        self.state = val

    def write(self) -> None:
        """ Write the value of `state` to the modbus server """
        if self.client.connect():
            self.client.write_coil(self.coil, self.state)
    def read(self) -> bool:
        """
        Read the value of the system from the modbus server

        Returns:
            bool: state of modbus system
        """
        if self.client.connect():
            result = self.client.read_coils(self.coil, 0)
            return result.bits[0]