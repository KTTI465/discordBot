import os
import discord
from discord.ext import commands

async def _loadFiles(bot:commands.Bot):
    files=os.listdir('./cogs')
    for i, filename in enumerate(files, 1):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"[{i}/{len(files)-1}] Successfully loaded : {filename[:-3]}")
            except Exception as e:
                print(f"[{i}/{len(files)-1}] {e}")
    files=os.listdir('./s_cogs')
    for i, filename in enumerate(files, 1):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f's_cogs.{filename[:-3]}')
                print(f"ad[{i}/{len(files)-1}] Successfully loaded : {filename[:-3]}")
            except Exception as e:
                print(f"ad[{i}/{len(files)-1}] {e}")

async def loadBot(bot:commands.Bot):
    print("init...")
    await bot.change_presence(activity=discord.Game("Init..."), status=discord.Status.idle)
    await _loadFiles(bot=bot)
    for guild in bot.guilds:
        await bot.tree.sync(guild=guild)
    await bot.tree.sync()
    print("ready")
    await bot.change_presence(activity=discord.Game("Ready"), status=discord.Status.online)

async def _reLoadFiles(bot:commands.Bot):
    files=os.listdir('./cogs')
    for i, filename in enumerate(files, 1):
        if filename.endswith('.py'):
            try:
                await bot.reload_extension(f'cogs.{filename[:-3]}')
                print(f"[{i}/{len(files)-1}] Successfully reloaded : {filename[:-3]}")
            except Exception as e:
                print(f"[{i}/{len(files)-1}] {e}")

async def reLoadBot(bot:commands.Bot):
    print("init...")
    await bot.change_presence(activity=discord.Game("Init..."), status=discord.Status.idle)
    await _reLoadFiles(bot=bot)
    for guild in bot.guilds:
        await bot.tree.sync(guild=guild)
    await bot.tree.sync()
    print("ready")
    await bot.change_presence(activity=discord.Game("Ready"), status=discord.Status.online)