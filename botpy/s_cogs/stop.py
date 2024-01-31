import discord
from discord import app_commands
from discord.ext import  commands
from discord.ext.tasks import Loop
from env.allow_user import AllowUser

class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="stop", description="admin only")
    async def stop(self, ctx: discord.Interaction):
        allow_user=AllowUser()
        print(f'stop command by {ctx.user}')
        if allow_user.user_auth(ctx.user.id):
            await ctx.response.send_message("bye", ephemeral=True)
            await ctx.client.close()
        else:
            await ctx.response.send_message(f"You do not have permission to execute the [{ctx.command.name}] command", ephemeral=True)

async def setup(bot:commands.Bot):
    await bot.add_cog(Stop(bot))