import discord
from discord import app_commands
from discord.ext import  commands
import datetime
from discord.ui import TextInput, Modal
from lib.dbms import DBMS
from lib.mail import create_mail

class Regist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="regist_user", description="Register as a user")
    async def regist(self, ctx: discord.Interaction):
        print(f'regist command by {ctx.user}')
        modal = RegistModal()
        await ctx.response.send_modal(modal)

class RegistModal(Modal, title='Register'):
    regist = TextInput(label='Mail Address' , style=discord.TextStyle.short, placeholder="xxxxxx@xxx.xxx", required=True)

    async def on_submit(self, ctx: discord.Interaction):
        await ctx.response.defer()
        dbms=DBMS()
        res = dbms.set_token(user_id=ctx.user.id, user_name=ctx.user.name)
        if res:
            embed = discord.Embed(title=self.title, description=f"**Successfully registered!**", timestamp=datetime.datetime.now(), color=discord.Color.green())
            embed.set_author(name=ctx.user, icon_url=ctx.user.avatar)
            embed.add_field(name="", value="The verification code has been sent to the email address you entered.\nPlease use the </verify:1161617836280660010> command to authenticate.\nThe email address will only be used to send the verification code.")
            create_mail(
                mail=self.regist.value, 
                subject="The verification code", 
                mailText=f"Please enter the code described below.\n\n{dbms.get_token(user_id=ctx.user.id)} \n\nThis email is for transmission only.")
            await ctx.followup.send(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title=self.title, description=f"**Faild...**", timestamp=datetime.datetime.now(), color=discord.Color.red())
            embed.set_author(name=ctx.user, icon_url=ctx.user.avatar)
            embed.add_field(name="", value="The user is already registered.\n If you have not yet authenticated, please use the </verify:1161617836280660010> command to do so.")
            await ctx.followup.send(embed=embed, ephemeral=True)
    

        
async def setup(bot:commands.Bot):
    await bot.add_cog(Regist(bot))