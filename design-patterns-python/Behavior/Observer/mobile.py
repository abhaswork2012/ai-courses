from observer import Observer

class Mobile(Observer):
    def update(self, temp: float) -> None:
        print(f"Mobile: The temperature is now {temp} degrees.")