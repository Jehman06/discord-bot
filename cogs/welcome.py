import discord
from discord.ext import commands
import json

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Get the channel ID
        welcome_channel_id = self.get_welcome_channel(member.guild)

        if welcome_channel_id:
            # Get the channel object
            welcome_channel = member.guild.get_channel(welcome_channel_id)

            if welcome_channel:
                welcome_message = f"Welcome to {member.guild.name}, {member.mention} 🎉!"
                await welcome_channel.send(welcome_message)

    def get_welcome_channel(self, guild):
        # Load configuration and get the welcome channel ID for the guild
        config = self.load_config()
        return config.get("welcome_channels", {}).get(str(guild.id))

    @commands.command(name="setwelcomechannel")
    @commands.has_permissions(administrator=True)
    async def set_welcome_channel(self, ctx, channel: discord.TextChannel = None):
        # Load configuration
        config = self.load_config()

        if not channel:
            # If channel is not provided, use the channel where the command was invoked
            channel = ctx.channel

        # Update configuration with the new welcome channel ID
        config["welcome_channels"] = {
            **config.get("welcome_channels", {}),
            str(ctx.guild.id): channel.id
        }

        # Save the updated configuration
        self.save_config(config)
        await ctx.send(f"Welcome channel set to {channel.mention}")
        print(f"Configuration after setting welcome channel: {config}")

    @commands.command(name="unsetwelcomechannel")
    @commands.has_permissions(administrator=True)
    async def unset_welcome_channel(self, ctx):
        # Load configuration
        config = self.load_config()

        guild_id = str(ctx.guild.id)
        if guild_id in config["welcome_channels"]:
            # Remove the welcome channel entry from configuration
            del config["welcome_channels"][guild_id]
            self.save_config(config)
            await ctx.send("Welcome channel unset.")
        else:
            await ctx.send("No welcome channel set for this server.")

    def load_config(self):
        # Load the configuration from the JSON file
        try:
            with open("config.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is not found or has decoding error, return an empty configuration
            return {"welcome_channels": {}}

    def save_config(self, config):
        # Save the configuration to the JSON file
        with open("config.json", "w") as file:
            json.dump(config, file)

async def setup(bot):
    await bot.add_cog(Welcome(bot))