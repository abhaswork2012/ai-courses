from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controlTower import ControlTower


class Airplane:

    def __init__(
        self,
        flight_name: str,
        control_tower: ControlTower
    ):
        self.__flight_name = flight_name
        self.__control_tower = control_tower

    def send_message(self) -> None:
        self.__control_tower.send_message(self.__flight_name)

    def receive_message(self, flight_name: str) -> None:
        print(
            f"Received message from {flight_name} "
            f"to {self.__flight_name}"
        )

    def get_flight_name(self) -> str:
        return self.__flight_name