import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders = []
        self.check_reminder.start()

    @commands.command(name="remindme", help="Set a reminder. Format: !remindme <time> <message>")
    async def remindme(self, ctx, time, *, message):
        try:
            await ctx.message.delete(delay=0.1)

            # Parse the time input from the user
            duration = timedelta(seconds=int(time))
            reminder_time = datetime.utcnow() + duration

            # Store the reminder in a list
            self.reminders.append((ctx.author.id, ctx.guild.id, reminder_time, message))

            # Send confirmation to the server channel but make it ephemeral
            await ctx.author.send(f"Got it! I will remind you about '{message}' in {time} seconds ({ctx.guild.name})")

        except ValueError:
            await ctx.author.send(f"Invalid time format. Please use an integer for seconds ({ctx.guild.name})")

    @tasks.loop(seconds=10)
    async def check_reminder(self,):
        current_time = datetime.utcnow()

        for reminder in self.reminders:
            user_id, guild_id, reminder_time, message = reminder
            guild = self.bot.get_guild(guild_id)

            if current_time >= reminder_time:
                user = self.bot.get_user(user_id)

                if user and guild:
                    # Send the reminder as a private message
                    await user.send(f"Reminder for {guild.name}: {message}")

                # Remove the reminder from the list
                self.reminders.remove(reminder)

    async def cog_unload(self):
        await self.check_reminder.stop()

async def setup(bot):
    await bot.add_cog(Tools(bot))
