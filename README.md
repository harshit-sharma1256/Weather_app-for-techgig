# Weather_app-using-github-copilot
# Weather Forecast Tool 

This command-line tool and web application provide the current weather forecast for a specified city. It leverages the OpenWeatherMap API to fetch weather data and displays the information such as main weather, description, temperature, humidity, wind speed, visibility, and dew point.

## Features

- Retrieves the current weather forecast for a specified city.
- Displays weather information including main weather, description, temperature, humidity, wind speed, visibility, and dew point.
- Handles incorrect city names and provides appropriate error messages.
- Utilizes the OpenWeatherMap API for fetching weather data.
- Supports both command-line and web application interfaces.
- Built with Python and leverages the Streamlit library for the web application.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/weather-forecast-tool.git
   ```

2. Navigate to the project directory:
   ```
   cd weather-forecast-tool
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Command-line Tool

Run the following command to use the command-line tool:

```
python weather_tool.py
```

Enter the name of a city when prompted, and the weather forecast will be displayed in the terminal.

### Web Application

Run the following command to start the web application:

```
streamlit run weather_app.py
```

Open the provided URL in your web browser. Enter the name of a city and click the "Get Weather Forecast" button to retrieve and display the weather forecast.

## API Configuration

To use the OpenWeatherMap API, you need to obtain an API key. Follow these steps:

1. Go to the [OpenWeatherMap website](https://openweathermap.org/) and create an account.
2. After logging in, navigate to your account dashboard and find the API keys section.
3. Generate a new API key and copy it.
4. Open the `weather_tool.py` file and replace `'YOUR_API_KEY'` with your actual API key.

## Limitations

- The tool currently supports fetching weather data for a single city at a time.
- It relies on the accuracy and availability of the OpenWeatherMap API.
- The visibility data is provided in kilometers, and the dew point is in Celsius.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the content as per your project's specifics. The above README.md file provides an overview of the tool, installation instructions, usage guidelines, API configuration details, limitations, and information on contributing and licensing.
