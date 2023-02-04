import discord
from discord import app_commands
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
GUILD_ID = discord.Object(os.getenv('GUILD_ID'))

class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "eric",
                           description = "If you don't know how to correct type friend's name",
                           with_app_command = True)
    async def eric(self, ctx: commands.Context) -> None:
        await ctx.send(embed=discord.Embed(title="His name is \nERIK \nE R I K\nERIK"), delete_after=5.0)

    @commands.hybrid_command(name = "wordle",
                           description = "Play wordle!",
                           with_app_command = True)
    async def wordle(self, ctx: commands.Context) -> None:
        with open('wordle_rules.txt') as wordle_rules:
            await ctx.send(embed=discord.Embed(description = wordle_rules.read()), delete_after=5.0)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Fun(bot))
