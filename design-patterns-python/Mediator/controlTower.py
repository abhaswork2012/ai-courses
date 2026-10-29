from typing import TYPE_CHECKING
from atc import AirTrafficControl

if TYPE_CHECKING:
    from air import Airplane


class ControlTower(AirTrafficControl):

    def __init__(self):
        self.__airplanes: list[Airplane] = []

    def register(self, airplane: Airplane) -> None:
        self.__airplanes.append(airplane)

    def send_message(self, flight_name: str) -> None:
        for airplane in self.__airplanes:
            if airplane.get_flight_name() != flight_name:
                airplane.receive_message(flight_name)