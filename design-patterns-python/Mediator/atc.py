from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from air import Airplane


class AirTrafficControl(ABC):

    @abstractmethod
    def register(self, airplane: Airplane) -> None:
        pass

    @abstractmethod
    def send_message(self, flight_name: str) -> None:
        pass