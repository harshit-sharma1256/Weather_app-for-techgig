#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing necessary libraries
import requests
import json
import streamlit as st


# In[2]:


#Function for getting api key
def get_api_key():
    with open('config.txt', 'r') as file:
        api_key = file.readline().strip()
    return api_key


# In[3]:


#Wrtting function for retrieve weather data for a specified city using the OpenWeatherMap API
def get_weather_forecast(city):
    api_key = get_api_key()  # Getting your OpenWeatherMap API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    response = requests.get(base_url, params={'q': city, 'appid': api_key})

    if response.status_code == 200:
        weather_data = json.loads(response.text)  # Parsing the JSON response

        return weather_data
    else:
        print('Please enter a valid city name.')  # Error handling for failed API request
        return None


# In[4]:


#Function for conversion of temperature from k to c
def convert_kelvin_to_celsius(temperature_kelvin):
    return temperature_kelvin - 273.15  # Conversion formula from Kelvin to Celsius


# In[5]:


#Function for display the weather forcast of the city
def display_weather_forecast(weather_data):
    if weather_data:
        city_name = weather_data['name']
        weather_main = weather_data['weather'][0]['main']
        weather_description = weather_data['weather'][0]['description']
        temperature = convert_kelvin_to_celsius(weather_data['main']['temp'])  # Converting temperature from Kelvin to Celsius
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        st.write(f'Weather forecast for {city_name}:')
        st.write(f'  - Main weather: {weather_main}')
        st.write(f'  - Description: {weather_description}')
        st.write(f'  - Temperature: {temperature:.2f}°C')  # Display temperature with two decimal places
        st.write(f'  - Humidity: {humidity}%')
        st.write(f'  - Wind speed: {wind_speed} m/s')
    else:
        st.error('No weather data available.')  # Error handling for missing weather data




# In[6]:


#Main function
def main():
    st.title('Weather Forecast Tool')  # Set the title of the web application

    try:
        city_name = st.text_input('Enter the name of a city')  # Create a text input field to enter the city name
        if st.button('Get Weather Forecast'):  # Create a button to trigger weather forecast retrieval
            weather_data = get_weather_forecast(city_name)  # Get the weather forecast data for the entered city
            display_weather_forecast(weather_data)  # Display the weather forecast

    except ValueError:
        st.error('Please enter a valid city name.')  # Error handling for incorrect city name


if __name__ == '__main__':
    main()


# In[ ]:




