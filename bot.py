import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        # Define intents
        intents = discord.Intents.all()

        # Pass intents to super().__init__
        super().__init__(command_prefix, intents=intents)

        # Set initial_extensions as an attribute of the bot
        self.initial_extensions = ['cogs.general', 'cogs.fun', 'cogs.poll']

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        await self.load_extensions()
        print("Loaded extensions:")
        for extension in self.extensions:
            print(f" - {extension}")
        print("Bot is ready!")

    async def load_extensions(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)

def main():
    # Load environment variables
    load_dotenv()

    # Get bot's token from the environment variable
    TOKEN = os.getenv('DISCORD_TOKEN')

    # Create an instance of the custom bot class
    bot = MyBot(command_prefix='!')

    # Run the bot
    bot.run(TOKEN)

if __name__ == "__main__":
    main()