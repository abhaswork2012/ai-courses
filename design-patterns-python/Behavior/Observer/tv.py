from observer import Observer

class TV(Observer):
    def update(self, temp: float) -> None:
        print(f"TV: The temperature is now {temp} degrees.")