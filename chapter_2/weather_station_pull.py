"""Observer pattern: Weather station app."""


class Subject:
    def __init__(self) -> None:
        self.observers = set()

    def register_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.discard(observer)

    def notify_observer(self, observer):
        observer.update()

    def notify_observers(self):
        for observer in self.observers:
            self.notify_observer(observer)


class WeatherData:
    def __init__(self) -> None:
        self.temp = None
        self.humidity = None
        self.pressure = None
        self.subject = Subject()

    def get_temp(self):
        return self.temp

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def set_measurements(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def register_observer(self, observer):
        self.subject.register_observer(observer)

    def remove_observer(self, observer):
        self.subject.remove_observer(observer)

    def measurements_changed(self):
        self.subject.notify_observers()


class Display:
    def __init__(self, weather_data: WeatherData) -> None:
        self.temp = None
        self.humidity = None
        self.pressure = None
        self.weather_data = weather_data
        self.register()

    def register(self):
        self.weather_data.register_observer(self)

    def unregister(self):
        self.weather_data.remove_observer(self)

    def update(self):
        raise NotImplementedError("Set this in each class.")
        self.temp = self.weather_data.get_temp()
        self.humidity = self.weather_data.get_humidity()
        self.pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        raise NotImplementedError("Make the display...")


class CurrentConditionsDisplay(Display):
    def update(self):
        self.temp = self.weather_data.get_temp()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self):
        print(f"Current conditions... temp: {self.temp}, humidity: {self.humidity}")


class StatisticsDisplay(Display):
    def __init__(self, weather_data: WeatherData) -> None:
        super().__init__(weather_data)
        self.temps = []

    def update(self):
        self.temp = self.weather_data.get_temp()
        self.display()

    def display(self):
        self.temps.append(self.temp)
        average_tmp = sum(self.temps) / len(self.temps)
        min_tmp = min(self.temps)
        max_tmp = max(self.temps)
        print(f"Avg/Max/Min temperature = {average_tmp:.1f}/{max_tmp}/{min_tmp}")


class ForecastDisplay(Display):
    def __init__(self, weather_data: WeatherData) -> None:
        super().__init__(weather_data)
        self.previous_temp = None
        self.previous_humidity = None
        self.previous_pressure = None

    def update(self):
        self.temp = self.weather_data.get_temp()
        self.humidity = self.weather_data.get_humidity()
        self.pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        print("Forecast: I'm not sure how to implement this...")
        self.previous_temp = self.temp
        self.previous_humidity = self.humidity
        self.previous_pressure = self.previous_pressure


if __name__ == "__main__":
    weather_data = WeatherData()
    conditions_display = CurrentConditionsDisplay(weather_data)
    stats_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    weather_data.set_measurements(1, 2, 3)
    forecast_display.unregister()
    weather_data.set_measurements(75, 30, 10)
