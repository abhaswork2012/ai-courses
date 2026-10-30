from abc import ABC, abstractmethod


class Chair(ABC):

    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):

    @abstractmethod
    def lie_on(self):
        pass