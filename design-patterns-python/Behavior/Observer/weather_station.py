from observer import Observer
from typing import List

class WeatherStation:
    def __init__(self):
        self.__temperature: float = 0.0
        self.__observers: List[Observer] = []
        
    def add_observer(self, observer: Observer):
        self.__observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)
    
    def update_temperature(self, temp: float):
        self.__temperature = temp
        self.notify_observers()
    
    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__temperature)