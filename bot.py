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
        self.initial_extensions = ['cogs.fun']

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

    @commands.command(name="keyword")
    async def cmd_keyword(self, ctx):
        # Respond to the keyword with a message
        await ctx.send("You used the keyword! Try !meme or !commands")

    @commands.command(name="commands")
    async def cmd_list_commands(self, ctx):
        command_list = [command.name for command in self.commands]
        await ctx.send(f"Available commands: {', '.join(command_list)}")

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