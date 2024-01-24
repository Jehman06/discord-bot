import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class RandomContentGenerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="generate_content")
    async def generate_content(self, ctx):
        # Content generation logic here
        await ctx.send('Random content generated!')

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        # Define intents
        intents = discord.Intents.all()

        # Pass intents to super().__init__
        super().__init__(command_prefix, intents=intents)

        # Initialize your cogs here
        self.add_cog(RandomContentGenerator(self))

# Load environment variables
load_dotenv()

# Get bot's token from the environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Create an instance of custom bot class
bot = MyBot(command_prefix='!')

# Event to run when the bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    await bot.add_cog(RandomContentGenerator(bot))

# Run the bot
bot.run(TOKEN)