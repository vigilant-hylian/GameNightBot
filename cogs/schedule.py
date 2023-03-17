""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class Schedule(commands.Cog, name="schedule"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="getschedules",
        description="Lists all the currently set-up games.",
    )
    # This will only allow owners of the bot to execute the command -> config.json
    @checks.is_owner()
    async def getschedules(self, context: Context, scope: str):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # Do your stuff here

        # Don't forget to remove "pass", I added this just because there's no content in the method.
        print(scope)
        pass


async def setup(bot):
    await bot.add_cog(Schedule(bot))
