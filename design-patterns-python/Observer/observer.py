from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temp: float) -> None:
        pass