import discord
from discord.ext import commands
import matplotlib.pyplot as plt
from io import BytesIO

class Polls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.polls = {}

    @commands.command(name="createpoll", help='Format: !createpoll <question> <answer 1> <answer 2> <...>')
    async def create_poll(self, ctx, question, *options):
        poll_id = len(self.polls) + 1
        self.polls[poll_id] = {"question": question, "options": options, "votes": {option: 0 for option in options}}

        poll_message = f"**Poll #{poll_id}**: {question}\n"
        for i, option in enumerate(options, 1):
            poll_message += f":regional_indicator_{chr(96+i)}: {option}\n"

        poll_message += "\nReact with the corresponding emojis to vote!"
        poll_message = await ctx.send(poll_message)

        for i, _ in enumerate(options, 1):
            emoji = chr(0x1F1E6 + i - 1)
            await poll_message.add_reaction(emoji)

    @commands.command(name="pollgraph", help="Format: !pollgraph pollnumber")
    async def poll_graph(self, ctx, poll_id):
        # Check if the poll_id is valid
        try:
            poll_id = int(poll_id)
        except ValueError:
            await ctx.send("Invalid poll_id. Please provide a valid integer.")
            return

        if poll_id not in self.polls:
            await ctx.send("Poll not found. Please provide a valid poll_id.")
            return

        # Get poll data
        question = self.polls[poll_id]["question"]
        options = self.polls[poll_id]["options"]
        votes = [self.polls[poll_id]["votes"][option] for option in options]

        # Plot the bar graph
        plt.bar(options, votes)
        plt.xlabel("Options")
        plt.ylabel("Votes")
        plt.title(f"Poll #{poll_id} Results - {question}")

        # Save the plot to a BytesIO object
        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)

        # Send the plot as an image
        graph_file = discord.File(image_stream, filename="poll_graph.png")
        await ctx.send(file=graph_file)

        # Close the plot to free up resources
        plt.close()

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # Check if the reaction is added by a bot (including the bot itself)
        if user.bot:
            return

        # Check if the reaction message is a poll message
        history = []
        async for message in reaction.message.channel.history(limit=100):
            history.append(message)

        if reaction.message.id not in [message.id for message in history]:
            return

        # Extract poll_id from the message content using a regular expression
        import re
        match = re.search(r'Poll #(\d+)', reaction.message.content)
        if not match:
            if str(reaction.emoji) == "🇧":  # Adjust the emoji representation as needed
                # Increment the vote count for the chosen option
                self.polls[poll_id]["votes"][option] += 1
            return

        poll_id = int(match.group(1))

        # Check if the emoji corresponds to a poll option
        for i, option in enumerate(self.polls[poll_id]["options"], 1):
            unicode_regional_indicator = chr(0x1F1E6 + i - 1)
            if str(reaction.emoji) == unicode_regional_indicator:
                # Increment the vote count for the chosen option
                self.polls[poll_id]["votes"][option] += 1

async def setup(bot):
    await bot.add_cog(Polls(bot))