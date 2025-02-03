# 🌤 Weather App

A Python-based desktop application that provides real-time weather updates using the OpenWeather API. Built with **PyQt5**, this app features an interactive user interface that fetches and displays weather details such as **temperature, condition, and an emoji representation of the weather**.

## 🚀 Features

- **Real-time Weather Data:** Fetches live weather updates for any city.
- **User-Friendly Interface:** Simple and intuitive PyQt5 GUI.
- **Weather Representation:** Displays temperature, description, and relevant emoji.
- **Unit Conversion:** Toggle between **Celsius (°C)** and **Fahrenheit (°F)**.
- **Error Handling:** Alerts users when the city name is invalid or API fails.

## 🏗 Technologies Used

- **Python** - Core programming language.
- **PyQt5** - GUI development.
- **requests** - API communication.
- **OpenWeatherMap API** - Fetches real-time weather data.

## 📂 Project Structure


## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app

**Install dependencies:**

   pip install -r requirements.txt
**Run the application:**
   python WeatherApp.py

## 🔑 API Key Configuration  
To fetch weather data, an API key from OpenWeatherMap is required.  

- 1. Get your API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).  
- 2. Open `WeatherApp.py` and replace the existing API key:  

   ```python
   self._weather_api = OpenWeatherAPI("your_api_key_here")

## 📌 How It WorksEnter a city name in the input field.
- Click "Get Weather" to fetch weather details.
- The app displays:
- Temperature (°C or °F)
- Weather description (e.g., "Cloudy")
- Emoji representation (e.g., ☀️ for sunny, 🌧️ for rainy)
- Click the unit button to switch between Celsius and Fahrenheit.
## 🎯 Object-Oriented Principles Used
- **Ecapsulation:** All UI and API functions are modularized.
- **Abstraction:** Users interact with a simple interface while complex API logic runs in the background.
- **Inheritance:** WeatherApp inherits from BaseApp to manage GUI.
- **Polymorphism:** Weather icons change dynamically based on weather conditions.
## 🔮 Future Enhancements
- **Weather Forecast:** Display upcoming weather predictions.
- **Geolocation:** Fetch weather based on the user's current location.
- **Dark Mode:** Improve UI for nighttime usage.
- **Multi-language** Support: Add support for different languages.

