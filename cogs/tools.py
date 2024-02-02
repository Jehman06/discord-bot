from discord.ext import commands, tasks
from datetime import datetime, timedelta
import re

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders = []
        self.check_reminder.start()

    @commands.command(name="remindme", help="Set a private reminder. Format: !remindme <1h30m or 30m> <message>")
    async def remind_me(self, ctx, time, *, message=""):
        try:
            # For private reminders, delete the command after 0.1 second
            await ctx.message.delete(delay=0.1)

            # Parse the time input from the user
            duration = self.parse_duration(time)
            reminder_time = datetime.utcnow() + duration

            # Store the reminder in a list with the target as "user"
            self.reminders.append(("user", ctx.author.id, ctx.guild.id, ctx.channel.id, reminder_time, message))

            # Send confirmation to the server channel
            await ctx.author.send(f'Got it! I will remind you about "{message}" in {time} ({ctx.guild.name})')

        except ValueError as e:
            await ctx.author.send(str(e))

    @commands.command(name="remindchannel", help="Set a channel reminder. Format: <time> <message>")
    async def remind_channel(self, ctx, time, *, message):
        try:
            # Parse the time input from the user
            duration = self.parse_duration(time)
            reminder_time = datetime.utcnow() + duration

            # Store the reminder in a list with the target as "channel"
            self.reminders.append(("channel", ctx.author.id, ctx.guild.id, ctx.channel.id, reminder_time, message))

            # Send confirmation to the server channel
            await ctx.send(f'Got it! I will remind the channel about "{message}" in {time}')

        except ValueError as e:
            await ctx.send(str(e))

    def parse_duration(self, time):
        # Parse a flexible time format (e.g., 1h30m, 2h, 30m)
        pattern = re.compile(r'(?:(\d+)h)?(?:(\d+)m)?')
        match = pattern.match(time)
        
        if not match:
            raise ValueError("Invalid time format. Please use a valid format like 1h30m, 2h, 30m")

        hours = int(match.group(1) or 0)
        minutes = int(match.group(2) or 0)

        return timedelta(hours=hours, minutes=minutes)

    @tasks.loop(seconds=10)
    async def check_reminder(self):
        current_time = datetime.utcnow()

        for reminder in self.reminders:
            target, user_id, guild_id, channel_id, reminder_time, message = reminder
            guild = self.bot.get_guild(guild_id)
            user = self.bot.get_user(user_id)
            channel = guild.get_channel(channel_id) if guild else None

            if current_time >= reminder_time and guild and user and channel:
                if target == "user":
                    # Send the reminder as a private message
                    await user.send(f"❗Reminder for {guild.name}: {message}")
                elif target == "channel":
                    # Send the reminder to the entire channel
                    await channel.send(f"❗Reminder: {message}")

                # Remove the reminder from the list
                self.reminders.remove(reminder)

    async def cog_unload(self):
        await self.check_reminder.stop()

async def setup(bot):
    await bot.add_cog(Tools(bot))