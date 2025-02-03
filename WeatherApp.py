import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from abc import ABC, abstractmethod

class WeatherAPI(ABC):
    @abstractmethod
    def get_weather_data(self, city, unit):
        pass

class OpenWeatherAPI(WeatherAPI):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_data(self, city, unit):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={unit}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

class WeatherDisplay:
    def __init__(self, temperature_label, emoji_label, description_label):
        self.temperature_label = temperature_label
        self.emoji_label = emoji_label
        self.description_label = description_label

    def display_weather(self, data, unit):
        temperature = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        unit_symbol = "°F" if unit == "imperial" else "°C"
        self.temperature_label.setText(f"{temperature:.2f} {unit_symbol}")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description.capitalize())

    @staticmethod
    def get_weather_emoji(weather_id):
        match weather_id:
            case 200 | 201 | 202 | 210 | 211 | 212 | 221 | 230 | 231 | 232:
                return "⛈️"
            case 300 | 301 | 302 | 310 | 311 | 312 | 313 | 314 | 321:
                return "🌧️"
            case 500 | 501 | 502 | 503 | 504 | 511 | 520 | 521 | 522 | 531:
                return "🌧️"
            case 600 | 601 | 602 | 611 | 612 | 613 | 615 | 616 | 620 | 621 | 622:
                return "❄️"
            case 701 | 711 | 721 | 731 | 741 | 751 | 761 | 762 | 771 | 781:
                return "🌫️"
            case 800:
                return "☀️"
            case 801:
                return "🌤️"
            case 802:
                return "⛅"
            case 803 | 804:
                return "☁️"
            case _:
                return "❓"

class BaseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

class WeatherApp(BaseApp):
    def __init__(self):
        super().__init__()
        self._city_label = QLabel("Enter City Name", self)
        self._city_input = QLineEdit(self)
        self._get_weather_button = QPushButton("Get Weather", self)
        self._temperature_label = QLabel(self)
        self._emoji_label = QLabel(self)
        self._description_label = QLabel(self)
        self._unit_button = QPushButton("°F", self)
        self._unit = "imperial"
        self._city = ""
        self._weather_api = OpenWeatherAPI("078c127dd1b35bbb740a4908320c5fa3")
        self._weather_display = WeatherDisplay(self._temperature_label, self._emoji_label, self._description_label)
        self.setupUI()

    def setupUI(self):
        self.layout.addWidget(self._city_label)
        self.layout.addWidget(self._city_input)
        self.layout.addWidget(self._get_weather_button)
        self.layout.addWidget(self._temperature_label)
        self.layout.addWidget(self._emoji_label)
        self.layout.addWidget(self._description_label)
        self.layout.addWidget(self._unit_button)

        self._city_label.setAlignment(Qt.AlignCenter)
        self._city_input.setAlignment(Qt.AlignCenter)
        self._temperature_label.setAlignment(Qt.AlignCenter)
        self._emoji_label.setAlignment(Qt.AlignCenter)
        self._description_label.setAlignment(Qt.AlignCenter)

        self._city_label.setObjectName("city_label")
        self._city_input.setObjectName("city_input")
        self._get_weather_button.setObjectName("get_weather_button")
        self._temperature_label.setObjectName("temperature_label")
        self._emoji_label.setObjectName("emoji_label")
        self._description_label.setObjectName("description_label")
        self._unit_button.setObjectName("unit_button")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: italic;
            }
            QLabel#city_label {
                font-size: 40px;
                font-weight: bold;
            }
            QLineEdit#city_input {
                font-size: 20px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QPushButton#unit_button {
                font-size: 20px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: "Segoe UI Emoji";
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self._get_weather_button.clicked.connect(self.get_weather)
        self._unit_button.clicked.connect(self.toggle_unit)

    def toggle_unit(self):
        if self._unit == "imperial":
            self._unit = "metric"
            self._unit_button.setText("°C")
        else:
            self._unit = "imperial"
            self._unit_button.setText("°F")
        
        if self._city:
            self.get_weather()

    def get_weather(self):
        city = self._city_input.text().strip()
        if not city:
            self.display_error("City name cannot be empty")
            return

        self._city = city

        try:
            data = self._weather_api.get_weather_data(city, self._unit)
            self._weather_display.display_weather(data, self._unit)
        except requests.exceptions.RequestException as e:
            self.display_error(f"Error: {e}")
        except KeyError:
            self.display_error("Unexpected data format from API")

    def display_error(self, message):
        self._temperature_label.setStyleSheet("font-size: 30px; color: red;")
        self._temperature_label.setText(message)
        self._emoji_label.setText("")
        self._description_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())