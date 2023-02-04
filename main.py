import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
GUILD_ID = discord.Object(os.getenv('GUILD_ID'))

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents = discord.Intents.all(),
            command_prefix = '%')
        
        self.initial_extensions = [
            "cogs.misc.fun",
            "cogs.music.player"
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)

        await self.tree.sync()

    async def on_ready(self):
        print("Hello, I'm Hitori Gotou!")

bot = MyBot()
bot.run(BOT_API_TOKEN)
