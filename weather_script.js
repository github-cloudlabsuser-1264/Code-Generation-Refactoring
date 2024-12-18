const fetch = require('node-fetch');

const apiKey = 'da49a559801ae670191ceab2b1f9608c'; // Replace with your OpenWeatherMap API key
const city = 'London'; // Replace with the desired city name

const getWeatherData = async (city, apiKey) => {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.cod === 200) {
            const temperature = data.main.temp;
            const humidity = data.main.humidity;
            const weatherCondition = data.weather[0].description;

            console.log(`Temperature: ${temperature}°C`);
            console.log(`Humidity: ${humidity}%`);
            console.log(`Weather Condition: ${weatherCondition}`);
        } else {
            console.log(`Error: ${data.message}`);
        }
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
};

getWeatherData(city, apiKey);