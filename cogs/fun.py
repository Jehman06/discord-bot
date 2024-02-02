from discord.ext import commands
import requests

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # MEME
    @commands.command(name="meme")
    async def meme(self, ctx):
        # Send a request to the meme API
        response = requests.get("https://meme-api.com/gimme")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the JSON content from the response
            data = response.json()

            # Check if the "url" key is present in the JSON content
            if "url" in data:
                # Access the meme URL from the JSON content
                meme_url = data["url"]

                # Send the meme URL to the channel
                await ctx.send(f"Here's a meme: {meme_url}")
            else:
                # Handle the case where the "url" key is not present
                await ctx.send("Sorry, I couldn't fetch a meme at the moment. Try again later.")
        else:
            # Handle the case where the request was not successful
            await ctx.send("Sorry, I couldn't fetch a meme at the moment. Try again later.")

    # STORY
    @commands.command(name="story")
    async def story(self, ctx):
        response = requests.get("https://shortstories-api.onrender.com") # https://github.com/poseidon-code/shortstories-api

        if response.status_code == 200:
            data = response.json()

            if "story" in data:
                story = data["story"]
                await ctx.send(story)
                
                if "moral" in data:
                    moral = data["moral"]
                    await ctx.send("Moral of the story:")
                    await ctx.send(moral)
            else:
                await ctx.send("Sorry, try again later")
        else:
            await ctx.send("Sorry, try again later")

    # JOKE
    @commands.command(name="joke")
    async def joke(self, ctx):
        max_attempts = 3

        for _ in range(max_attempts):
            response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
        
            if response.status_code == 200:
                data = response.json()

                if "setup" in data and data["setup"]:
                    joke_setup = data["setup"]
                    await ctx.send(f"{joke_setup}")

                    if "delivery" in data:
                        joke_delivery = data["delivery"]
                        await ctx.send(f"{joke_delivery}")
                    return  # Exit the loop if a valid joke is found

async def setup(bot):
    await bot.add_cog(FunCommands(bot))