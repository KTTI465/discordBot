import discord
from discord import app_commands
from discord.ext import commands
import datetime
from env.config import Config
from discord.ui import Button, View, TextInput, Modal
from env.allow_user import AllowUser
from lib.dbms import DBMS

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name="verify", description="verify user")
    async def verify(self, ctx: discord.Interaction):
        print(f'verify command by {ctx.user}')
        modal = VerifyModal()
        await ctx.response.send_modal(modal)

class VerifyModal(Modal, title='Verify'):
    verify_ID = TextInput(label='Verify ID', style=discord.TextStyle.short, placeholder="xxxx", required=True)

    async def on_submit(self, ctx: discord.Interaction):
        config=Config()
        dbms=DBMS()

        async def callback_a(ctx:discord.Interaction):
            modal=AdminModal()
            await ctx.response.send_modal(modal)

        async def callback_b(ctx:discord.Interaction):
            await ctx.response.send_message("Did not register", ephemeral=True)
            

        if str(self.verify_ID.value) == config.adminpassword:
            button1=Button(label="Add Admin", style=discord.ButtonStyle.green, emoji="✅")
            button2=Button(label="Don't", style=discord.ButtonStyle.danger, emoji="❎")
            button1.callback=callback_a
            button2.callback=callback_b
            view=View()
            view.add_item(button1)
            view.add_item(button2)
            await ctx.response.send_message(view=view, ephemeral=True, delete_after=10)
        else:
            res = dbms.auth_token(user_id=ctx.user.id, token=self.verify_ID.value)
            if res == "Notfound":
                embed = discord.Embed(title=self.title, description=f"**{self.verify_ID.label}**\n Faild...\n User ID not found", timestamp=datetime.datetime.now(), color=discord.Color.red())
                embed.set_author(name=ctx.user, icon_url=ctx.user.avatar)
                await ctx.response.send_message(embed=embed, ephemeral=True)
            elif res == "Faild":
                embed = discord.Embed(title=self.title, description=f"**{self.verify_ID.label}**\n Faild...\n Incorrect token", timestamp=datetime.datetime.now(), color=discord.Color.red())
                embed.set_author(name=ctx.user, icon_url=ctx.user.avatar)
                await ctx.response.send_message(embed=embed, ephemeral=True)
            elif res == "Already":
                embed = discord.Embed(title=self.title, description=f"**{self.verify_ID.label}**\n Faild...\n Already authenticated", timestamp=datetime.datetime.now(), color=discord.Color.red())
                embed.set_author(name=ctx.user, icon_url=ctx.user.avatar)
                await ctx.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = discord.Embed(title=self.title, description=f"**{self.verify_ID.label}**\n Successfully authenticated!", timestamp=datetime.datetime.now(), color=discord.Color.green())
                embed.set_author(name=ctx.user, icon_url=ctx.user.avatar)
                await ctx.response.send_message(embed=embed, ephemeral=True)


class AdminModal(Modal, title='Add Admin User'):
    Admin_Name = TextInput(label='User Name', style=discord.TextStyle.short, placeholder="USERNAME", required=True)
    Admin_ID = TextInput(label='User ID to be added', style=discord.TextStyle.short, placeholder="xxxxxxxxxxxxxxxxxx", required=True)

    async def on_submit(self, ctx: discord.Interaction):
        embed = discord.Embed(title=self.title, description=f"**Admin added**\n {self.Admin_ID}\n{self.Admin_Name}", timestamp=datetime.datetime.now(), color=discord.Color.blue())
        allowuser=AllowUser()
        try:
            allowuser.add_user(user_name=str(self.Admin_Name.value), user_id=int(self.Admin_ID.value))
            await ctx.response.send_message(embed=embed, ephemeral=True)
        except :
            await ctx.response.send_message("Registration failed", ephemeral=True)

async def setup(bot:commands.Bot):
    await bot.add_cog(Verify(bot))