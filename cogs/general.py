from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="keyword")
    async def cmd_keyword(self, ctx):
        # Respond to the keyword with a message
        await ctx.send("You used the keyword! Try !commands to see a list of all commands")

    @commands.command(name="commands")
    async def cmd_list_commands(self, ctx):
        command_list = [command.name for command in self.bot.commands]
        await ctx.send(f"Available commands: {', '.join(command_list)}")

async def setup(bot):
    await bot.add_cog(General(bot))