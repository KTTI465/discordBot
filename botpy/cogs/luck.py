import discord
from discord import app_commands
from discord.ext import commands
import random

class Luck(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @app_commands.command(name="luck", description="今日の運勢やいかに...")
    async def luck(self, ctx:discord.Interaction):
        print(f'luck command by {ctx.user}')
        fortune_list = ['大吉', '中吉', '吉', '小吉',
                        '末吉', '凶', '大凶', '判断が遅い', 'SSR', 'UR']
        fortune_length = len(fortune_list)

        await ctx.response.send_message(content=
            "今日の運勢は【" + fortune_list[random.randint(0, fortune_length - 1)] + "】だよ！", ephemeral=True)
        
async def setup(bot:commands.Bot):
    await bot.add_cog(Luck(bot))