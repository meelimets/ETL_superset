import requests

# Your OpenWeatherMap API key
api_key = '436069825c3b72ae673ef95a4420fc00'

# API endpoint for current weather data
url = f'http://api.openweathermap.org/data/2.5/weather?q=Tartu&appid={api_key}&units=metric'

# Send request to the API
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Extract relevant weather information
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    
    # Print the current weather
    print(f'Temperature in Tartu: {temperature}°C')
    print(f'Weather: {weather_description}')
else:
    print('Failed to fetch weather data')

