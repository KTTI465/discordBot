import discord
from discord import app_commands
from discord.ext import commands
from lib.mail import create_mail
from env.allow_user import AllowUser

class Sendmail(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name="send_mail", description="debug send mail")
    async def mail(self, ctx: discord.Interaction):
        print(f'send_mail command by {ctx.user}')
        allow_user=AllowUser()
        if allow_user.user_auth(ctx.user.id):
            modal = MailModal()
            await ctx.response.send_modal(modal)
        else:
            await ctx.response.send_message(f"You do not have permission to execute the [{ctx.command.name}] command", ephemeral=True)

class MailModal(discord.ui.Modal, title='Send GMail'):
    mail_address = discord.ui.TextInput(label='Address', style=discord.TextStyle.short, placeholder="xxxxxx@xxx.xxx", required=True)
    mail_subject = discord.ui.TextInput(label='Subject', style=discord.TextStyle.short, required=True)
    mail_Text = discord.ui.TextInput(label='Text', style=discord.TextStyle.paragraph, required=True)

    async def on_submit(self, ctx: discord.Interaction):
        await ctx.response.defer()
        try:
            create_mail(mail=self.mail_address.value, subject=self.mail_subject.value, mailText=self.mail_Text.value)
            await ctx.followup.send("send mail", ephemeral=True)
        except:
            await ctx.followup.send("faild", ephemeral=True)

async def setup(bot:commands.Bot):
    await bot.add_cog(Sendmail(bot))