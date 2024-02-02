from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # WEATHER
    @commands.command(name="weather", help="Check the weather in a specific location. Format: !weather <city>")
    async def weather(self, ctx, *, city):
        try:
            weather_data = await self.fetch_weather(city)

            await ctx.send(f"Current weather in {city}, {weather_data['sys']['country']}: \n Weather: {weather_data['weather'][0]['main']} \n Temperature: {weather_data['main']['temp']}°F \n Feels like: {weather_data['main']['feels_like']}°F \n Max temperature: {weather_data['main']['temp_max']}°F \n Min temperature: {weather_data['main']['temp_min']}°F")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

    async def fetch_weather(self, city):
        # Load the environment variable for the API key
        load_dotenv()
        # Get bot's token from the environment variable
        KEY = os.getenv('OWKey')

        # Send a request to the OpenWeather API
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={KEY}")

        if response.status_code == 200:
            data = response.json()
        else:
            raise Exception(f"Unable to check for the weather. Status code: {response.status_code}")

        return data
    
async def setup(bot):
    await bot.add_cog(Info(bot))