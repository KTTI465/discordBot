import os
import discord
from discord.ext import commands
import discord.app_commands
from env.config import Config
import asyncio
from lib.setupper import loadBot

intents=discord.Intents.all()
intents.members=True
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    status=discord.Status.offline,
    help_command=None,
)

config = Config()

TOKEN = config.token

@bot.event
async def on_ready():
    await loadBot(bot)

async def main():
    await bot.start(TOKEN)

asyncio.run(main())