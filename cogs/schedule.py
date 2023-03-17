""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import discord
from discord.ext import commands
from discord.ext.commands import Context
from datetime import datetime, timedelta
import pytz
import time
import math

from helpers import db_manager, checks


class Schedule(commands.Cog, name="schedule"):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(
        name="whenisgame",
        description="Lists all the currently set-up games.",
    )
    async def whenisgame(self, context: Context):
        """
        This is a slash command to return a list of all the games currently stored in the database.

        :param context: The application command context.
        """
        games_list = await db_manager.get_schedules()
        embed = discord.Embed(
            title=f"Currently Running Games",
            description="The following games have been scheduled to be played! The next session is below in your local timezome.",
            color=0x299639
        )
        for game in games_list:
            current_time = datetime.now()
            next_session = datetime.fromtimestamp(game[2])
            while time.mktime(next_session.timetuple()) < time.mktime(current_time.timetuple()):
                next_session += timedelta(days=game[3])
            embed.add_field(name=f"{game[1]}", value=f"Next Session: <t:{math.trunc(datetime.timestamp(next_session))}>\n"
                f"Runs every: {game[3]} days\n"
                f"ID: {game[0]}\n", inline=False)
        await context.send(embed=embed)

    @commands.hybrid_command(
        name='add_game',
        description='Add a new game to the schedule.'
    )
    async def add_game(self, context: Context, gamename: str, repeat_in_x_days: int, year: int, month: int, day: int, hour: int, minute: int, tz: str):
        try:
            timezone = pytz.timezone(tz)
            game = datetime(year=year, month=month, day=day, hour=hour, minute=minute)
            utcgame = timezone.localize(game)
            utctime = math.trunc(time.mktime(utcgame.timetuple()))
        except pytz.UnknownTimeZoneError as e:
            embed = discord.Embed(
                title=f"Unknown Timezone",
                description=f"Error: {e}",
                color=0xff0000
            )
            await context.send(embed=embed)
            return
        except ValueError as e:
            embed = discord.Embed(
                title=f"Bad DateTime Input",
                description=f"Error: {e}",
                color=0xff0000
            )
            await context.send(embed=embed)
            return
        await db_manager.add_schedule(gamename, utctime, repeat_in_x_days)
        embed = discord.Embed(
            title=f"Added new game",
            description=f"{gamename}: Starting at <t:{utctime}>, repeating every {repeat_in_x_days} days.",
            color=0x299639
        )
        await context.send(embed=embed)


    @commands.hybrid_command(
            name='remove_game',
            description='Remove a new game from the schedule.'
        )
    async def remove_game(self, context: Context, entry_id: int):
        success = await db_manager.remove_schedule(entry_id)
        self.bot.logger.info(f'{success.rowcount}')
        if success.rowcount == 1:
            embed = discord.Embed(
                title=f"Deleted",
                description=f"Removed entry.",
                color=0x299639
            )
        else:
            embed = discord.Embed(
                title=f"Invalid Entry",
                description=f"Please check provided ID.",
                color=0xff0000
            )
        await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Schedule(bot))
