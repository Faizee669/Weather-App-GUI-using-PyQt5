# ✨ Weather App

A Python-based desktop application that provides real-time weather updates using the OpenWeather API. Built with **PyQt5**, this app features an interactive user interface that fetches and displays weather details such as **temperature, condition, and an emoji representation of the weather**.

## DEMO
![Image](https://github.com/user-attachments/assets/3915b797-d78d-4b7b-b8d0-3ddb56ed3bcb)

## 🚀 Features

- **Real-time Weather Data:** Fetches live weather updates for any city.
- **User-Friendly Interface:** Simple and intuitive PyQt5 GUI.
- **Weather Representation:** Displays temperature, description, and relevant emoji.
- **Unit Conversion:** Toggle between **Celsius (\u00b0C)** and **Fahrenheit (\u00b0F)**.
- **Error Handling:** Displays error messages for invalid city names or API failures.

## 🏰 Technologies Used

- **Python** - Core programming language.
- **PyQt5** - GUI development.
- **requests** - API communication.
- **OpenWeatherMap API** - Fetches real-time weather data.

## 📂 Project Structure

```
WeatherApp/
|-- WeatherApp.py   # Main application file
|-- README.md       # Documentation
|-- requirements.txt # Dependencies
```

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python WeatherApp.py
   ```

## 🔑 API Key Configuration  
To fetch weather data, an API key from OpenWeatherMap is required.  

- 1. Get your API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).  
- 2. Open `WeatherApp.py` and replace the existing API key:

   ```python
   self._weather_api = OpenWeatherAPI("your_api_key_here")
   ```
   **(Recommended: Store the API key in an environment variable for security.)**

## 📌 How It Works
- Enter a city name in the input field.
- Click "Get Weather" to fetch weather details.
- The app displays:
  - Temperature (\u00b0C or \u00b0F)
  - Weather description (e.g., "Cloudy")
  - Emoji representation (e.g., ☀️ for sunny, 🌧️ for rainy)
- Click the unit button to switch between Celsius and Fahrenheit.

## 🎯 Object-Oriented Principles Used
- **Encapsulation:** All UI and API functions are modularized.
- **Abstraction:** Users interact with a simple interface while complex API logic runs in the background.
- **Inheritance:** `WeatherApp` inherits from `BaseApp` to manage the GUI.

## 🔮 Future Enhancements
- **Weather Forecast:** Display upcoming weather predictions.
- **Geolocation:** Fetch weather based on the user's current location.
- **Dark Mode:** Improve UI for nighttime usage.
- **Multi-language Support:** Add support for different languages.

## 🤝 Contributing  

Contributions are welcome! If you'd like to contribute to this project, follow these steps:  

### 1. Fork the Repository  
Click the **Fork** button at the top-right of this repository to create a copy in your GitHub account.  

### 2. Clone the Repository  
Clone your forked repository to your local machine using:  

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

