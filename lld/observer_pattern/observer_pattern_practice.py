"""
Observer Pattern - Practice Exercise

Scenario: A Weather Station that collects temperature, humidity, and pressure.
Multiple displays (CurrentConditionsDisplay, StatisticsDisplay, ForecastDisplay)
should be updated automatically whenever the weather data changes.

Your Task:
1. Define the Observer interface (e.g., WeatherObserver with an update method).
2. Implement the Subject (WeatherStation) with attach, detach, and notify.
3. Implement at least two concrete observers that react to weather updates.
4. Use a push model: pass the new measurements to update() so observers don't need a reference to the subject.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


# ==========================================
# Data object (optional but good practice)
# ==========================================
@dataclass
class WeatherData:
    temperature: float
    humidity: float
    pressure: float


# ==========================================
# TODO 1: Define the Observer interface
# ==========================================
class WeatherObserver(ABC):
    """
    Define an abstract method that receives the new weather data (push model).
    Example: def update(self, data: WeatherData) -> None
    """
    @abstractmethod
    def update(self, data: WeatherData) -> None:
        ...
    


# ==========================================
# TODO 2: Implement the Subject (WeatherStation)
# ==========================================
class WeatherStation:
    """
    - Maintain a list of observers.
    - Provide attach(observer) and detach(observer).
    - Provide set_measurements(temperature, humidity, pressure) that updates
      internal state and calls notify.
    - notify() should call update(weather_data) on each observer.
    """
    def __init__(self) -> None:
        self._observers: List[WeatherObserver] = []
    
    def attach(self, observer: WeatherObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: WeatherObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, data: WeatherData) -> None:
        for observer in self._observers:
            observer.update(data)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        data = WeatherData(temperature=temperature, humidity=humidity, pressure=pressure)
        self.notify(data)


# ==========================================
# TODO 3: Implement Concrete Observers
# ==========================================
class CurrentConditionsDisplay:
    """
    Display current temperature and humidity when updated.
    """
    def __init__(self) -> None:
        self.temperature = 0.0
        self.humidity = 0.0
    
    def update(self, data: WeatherData) -> None:
        self.temperature = data.temperature
        self.humidity = data.humidity
        self.display()
    
    def display(self) -> None:
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")


class StatisticsDisplay:
    """
    Track min/max/avg temperature over time (simplified: just show current as min/max/avg for now,
    or keep a running list and compute stats).
    """
    def __init__(self) -> None:
        self.min_temperature = float('inf')
        self.max_temperature = float('-inf')
        self.total_temperature = 0.0
    
    def update(self, data: WeatherData) -> None:
        self.min_temperature = min(self.min_temperature, data.temperature)
        self.max_temperature = max(self.max_temperature, data.temperature)
        self.display()
    
    def display(self) -> None:
        print(f"Statistics: Min: {self.min_temperature}F, Max: {self.max_temperature}F")


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    # Uncomment and complete after implementing:
    #
    station = WeatherStation()
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()
    station.attach(current_display)
    station.attach(stats_display)
    
    station.set_measurements(72.5, 65.0, 1013.2)
    station.set_measurements(68.0, 70.0, 1012.1)
    
    station.detach(stats_display)
    station.set_measurements(75.0, 60.0, 1014.0)

    print("[!] Implement the TODOs to practice the Observer Pattern!")
