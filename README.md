# Weather Forecast Tool

This command-line tool and web application provide the current weather forecast for a specified city. It leverages the OpenWeatherMap API to fetch weather data and displays the information such as main weather, description, temperature, humidity, and wind speed.

## Features

- Retrieves the current weather forecast for a specified city.
- Displays weather information including main weather, description, temperature, humidity, wind speed, visibility, and dew point.
- Handles incorrect city names and provides appropriate error messages.
- Utilizes the OpenWeatherMap API for fetching weather data.
- Supports both command-line and web application interfaces.
- Built with Python and leverages the Streamlit library for the web application.

## Installation

Clone the repository:
```
git clone https://github.com/harshit-sharma1256/Weather_app-for-techgig.git
```

## Requirements

Make sure the following libraries are installed in your Python environment:

- Streamlit
- json
- requests

You can install these libraries by running the following command:
```
pip install streamlit json requests
```

## Usage

### Web Application

To run the web application, follow these steps:

1. Firstly, open your Anaconda Prompt.
2. Go to your project path:
   ```
   cd path/to/weather-forecast-tool
   ```
   Replace `path/to/weather-forecast-tool` with the actual path to the project directory.
3. Run the following command:
   ```
   streamlit run weather_app.py
   ```
4. After executing the command, the web application will start running locally.
5. Open your web browser and go to the provided URL (typically `http://localhost:8501`).
6. Enter the name of a city in the text input field and click the "Get Weather Forecast" button to retrieve and display the weather forecast.

### Command-Line Tool

To use the command-line tool, follow these steps:

1. Open your Anaconda Prompt or terminal.
2. Navigate to the project directory:
   ```
   cd path/to/weather-forecast-tool
   ```
   Replace `path/to/weather-forecast-tool` with the actual path to the project directory.
3. Run the following command:
   ```
   python weather_tool.py
   ```
4. Follow the prompts and enter the name of a city to get the weather forecast.

## API Configuration

To use the OpenWeatherMap API, you need to obtain an API key. Follow these steps:

1. Go to the [OpenWeatherMap website](https://openweathermap.org/) and create an account.
2. After logging in, navigate to your account dashboard and find the API keys section.
3. Generate a new API key and copy it.
4. Open the `weather_tool.py` file and replace `'YOUR_API_KEY'` with your actual API key.

## Limitations

- The tool currently supports fetching weather data for a single city at a time.
- It relies on the accuracy and availability of the OpenWeatherMap API.

## Output Images

Here are three sample output images from the Weather Forecast Tool:

1. Weather forecast for New York City:

   ![New York City](https://example.com/new_york_city.png)

2. Weather forecast for London:

   ![London](https://example.com/london.png)

3. Weather forecast for Sydney:

   ![Sydney](https://example.com/sydney.png)

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## Contact

For any inquiries or questions, you can reach me at harshit2531937@gmail.com.

In the "Output Images" section, replace the URLs (`https://example.com/new_york_city.png`, `https
