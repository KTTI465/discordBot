import discord
from discord import app_commands
from discord.ext import commands
import time

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name="ping", description="pong")
    async def ping (self, ctx:discord.Interaction):
        print(f'ping command by {ctx.user}')
        s_time = time.time()
        await ctx.response.send_message("計測中...", ephemeral=True)
        await ctx.edit_original_response(content=f"レイテンシ:{(time.time() - s_time)*1000:.3f}ms")

async def setup(bot:commands.Bot):
    await bot.add_cog(Ping(bot))