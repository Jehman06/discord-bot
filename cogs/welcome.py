import discord
from discord.ext import commands
import json

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Get the channel ID and welcome message for the guild
        welcome_channel_id, welcome_message = self.get_welcome_info(member.guild)

        if welcome_channel_id and welcome_message:
            # Get the channel object
            welcome_channel = member.guild.get_channel(welcome_channel_id)

            if welcome_channel:
                # Replace placeholders in the welcome message with member-specific information
                welcome_message = welcome_message.format(member=member, guild=member.guild)

                # Send the personalized welcome message
                await welcome_channel.send(welcome_message)

    def get_welcome_info(self, guild):
        # Load configuration and get the welcome channel ID and welcome message for the guild
        config = self.load_config()
        guild_id = str(guild.id)
        welcome_channel_id = config.get("welcome_channels", {}).get(guild_id)
        welcome_message = config.get("welcome_messages", {}).get(guild_id, "Welcome to {guild.name}, {member.mention} 🎉!")

        return welcome_channel_id, welcome_message
    
    # !setwelcomemessage
    @commands.command(name="setwelcomemessage", help="Admins only. Set a personalized welcome message.")
    @commands.has_permissions(administrator=True)
    async def set_welcome_message(self, ctx, *, message):
        # Load configuration
        config = self.load_config()

        guild_id = str(ctx.guild.id)
        # Update configuration with the new welcome message
        config["welcome_messages"] = {
            **config.get("welcome_messages", {}),
            guild_id: message
        }

        # Save the updated configuration
        self.save_config(config)
        await ctx.send("Personalized welcome message set.")
        print(f"Configuration after setting welcome message: {config}")

    # !setwelcomechannel
    @commands.command(name="setwelcomechannel", help="Admins only")
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

    # !unsetwelcomechannel
    @commands.command(name="unsetwelcomechannel", help="Admins only")
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
            return {"welcome_channels": {}, "welcome_messages": {}}

    def save_config(self, config):
        # Save the configuration to the JSON file
        with open("config.json", "w") as file:
            json.dump(config, file)

async def setup(bot):
    await bot.add_cog(Welcome(bot))