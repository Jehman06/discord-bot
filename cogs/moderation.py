from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # KICK
    @commands.command(name="kick", help="Kick a user from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason="No reason provided"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.display_name} has been kicked for: {reason}")

    # BAN
    @commands.command(name="ban", help="Ban a user from the server")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason="No reason provided"):
        await member.ban(reason=reason)
        await ctx.send(f"{member.display_name} has been banned for: {reason}")

    # Add more moderation commands

async def setup(bot):
    await bot.add_cog(Moderation(bot))