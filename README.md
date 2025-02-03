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
Get your API key from OpenWeatherMap.
**Open WeatherApp.py and replace the existing API key:**
   self._weather_api = OpenWeatherAPI("your_api_key_here")

