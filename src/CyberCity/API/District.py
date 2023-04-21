from .power import Power

class District():
    """
    The District Object
    """
    def __init__(self, name: str, global_power_coil: int):
        """
        Initializes the District object
        Args:
            name (str): Name of the District
            globalPowerCoil (int): Coil for power grid
        """
        self.name = name
        """ Name of the District """

        self.global_power = Power(self.name, global_power_coil)
        """ Power Object """

    def __str__(self) -> str:
        """
        State of the District String
        Returns:
            str: State of the District
        """
        return f'{self.name} => {self.global_power} '
