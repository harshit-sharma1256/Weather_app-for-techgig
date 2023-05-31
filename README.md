# Weather Forecast Tool

This command-line tool and web application provide the current weather forecast for a specified city. It leverages the OpenWeatherMap API to fetch weather data and displays the information such as main weather, description, temperature, humidity, and wind speed.

## Features

- Retrieves the current weather forecast for a specified city.
- Displays weather information including main weather, description, temperature, humidity, and wind speed.
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

You can install these libraries by running the following commandS:
```
pip install streamlit json requests
pip install -r requirements.txt
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

## API Configuration

To use the OpenWeatherMap API, you need to obtain an API key. Follow these steps:

1. Go to the [OpenWeatherMap website](https://openweathermap.org/) and create an account.
2. After logging in, navigate to your account dashboard and find the API keys section.
3. Generate a new API key and copy it.
4. Create a file named `config.txt` in the project directory.
5. Open the `config.txt` file and paste the API key on the first line.

## Limitations

- The tool currently supports fetching weather data for a single city at a time.
- It relies on the accuracy and availability of the OpenWeatherMap API.

## Output Images

Here are three sample output images from the Weather Forecast Tool:

1. Weather forecast for Bharatpur City:

   ![Bharatpur City](https://github.com/harshit-sharma1256/Weather_app-for-techgig/blob/9eb70595307567cbbfb60a525d1e68135614d765/op1.png)

2. Weather forecast for Rio:

   ![Rio](https://github.com/harshit-sharma1256/Weather_app-for-techgig/blob/9eb70595307567cbbfb60a525d1e68135614d765/op2.png)

3. Weather forecast for Wrong city entered:

   ![Wrong city](https://github.com/harshit-sharma1256/Weather_app-for-techgig/blob/9eb70595307567cbbfb60a525d1e68135614d765/op3.png)

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## Contact

For any inquiries or questions, you can reach me at harshit2531937@gmail.com.


