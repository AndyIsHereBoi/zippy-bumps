
import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands.flags import F
from nextcord import Client, Interaction, SlashOption, ChannelType, Message, slash_command
from nextcord.abc import GuildChannel
import nextcord
import os
import time
import datetime
import json

replace = os.path.basename(__file__)
thing = __file__
directory = thing.replace(f"/cogs/{replace}", '')
directory = directory + "/"

config_file = f"{directory}config.json"
import json
with open(config_file) as config_file:
    data = json.load(config_file)


config_file = f"{directory}config.json"
import json
with open(config_file) as config_file:
    data = json.load(config_file)

owners = data['owners']
token = data['token']
prefix = data['prefix']
logchnl = data['logchannel']
supportServer = data['supportServer']
botInvite = data['botInvite']
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command("help")
footerText = data['footerText']
ad_count_send = data['ad_count_send']


class Owner(commands.Cog):
    """Receives owner commands"""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    class Status(nextcord.ui.View):
        @nextcord.ui.button(label='Online', style=nextcord.ButtonStyle.green)
        async def one(button: nextcord.ui.Button, interaction: nextcord.Interaction):
            if interaction.user.id in owners:
                await bot.change_presence(status=nextcord.Status.online)
                await interaction.response.send_message("Edited status to Online.", ephemeral=True)
            else:
                await interaction.response.send_message("You cannot use this.", ephemeral=True)
                    
        @nextcord.ui.button(label='Idle', style=nextcord.ButtonStyle.blurple)
        async def two(button: nextcord.ui.Button, interaction: nextcord.Interaction):
            if interaction.user.id in owners:
                await bot.change_presence(status=nextcord.Status.idle)
                await interaction.response.send_message("Edited status to Idle.", ephemeral=True)
            else:
                await interaction.response.send_message("You cannot use this.", ephemeral=True)

        @nextcord.ui.button(label='DND', style=nextcord.ButtonStyle.red)
        async def three(button: nextcord.ui.Button, interaction: nextcord.Interaction):
            if interaction.user.id in owners:
                await bot.change_presence(status=nextcord.Status.dnd)
                await interaction.response.send_message("Edited status to DND.", ephemeral=True)
            else:
                await interaction.response.send_message("You cannot use this.", ephemeral=True)

    
    @slash_command(name="status",description="Change my status",guild_ids=[794684213697052712], force_global=True)
    async def status_command(self, interaction: Interaction, choice: str = SlashOption(name="type", description="Online, Idle, DND, Offline", choices={"Online": "Online", "Idle": "Idle","DND": "DND"})):
        await interaction.response.defer()
        if interaction.user.id in owners:
            if choice == "Online":
                await interaction.followup.send("Set status to Online")
                await self.bot.change_presence(status=nextcord.Status.online)
            if choice == "Idle":
                await interaction.followup.send("Set status to Idle")
                await self.bot.change_presence(status=nextcord.Status.idle)
            if choice == "DND":
                await interaction.followup.send("Set status to DND")
                await self.bot.change_presence(status=nextcord.Status.dnd)
        else:
            await interaction.followup.send("You must be a owner to perform this action.")

    @commands.command()
    async def status(self, ctx):
        if ctx.author.id in owners:
            await ctx.send('Select bot status:', view=Status())


    @commands.command(brief="[Owner Only] Set the bots watching activity")
    async def activity(self, ctx, activity):
        if ctx.author.id in owners:
            await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=activity))
                    
                    
    
    @commands.command(brief="[Owner Only] Delete messages")
    async def purge(self, ctx, ammount):
        if ctx.author.id in owners:
            ammount = int(ammount)
            if ammount > 100:
                await ctx.send("You can not purge more then 100 messages at a time.")
            elif ammount < 1:
                await ctx.send("You need to purge more then 0 messages.")
            else:
                ammount = int(ammount)
                await ctx.channel.purge(limit=ammount)


    
    @slash_command(name="activity",description="Change my playing status!",guild_ids=[859610420615446538], force_global=True)
    async def activity_command(self, interaction: Interaction, status: str):
        if interaction.user.id in owners:
            await interaction.response.defer()
            await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=f"{status}"))
            embed = nextcord.Embed(title="Changed status", description=f'to {status}', color=0xEE8700)
            embed.set_footer(text=footerText)
            await interaction.followup.send(embed=embed)

    
    @commands.command(brief="[Owner Only] send messages from bot")
    async def say(self, ctx, msg):
        if ctx.author.id in owners:
            await ctx.send(msg)

    @slash_command(name="say",description="Make me say something!",guild_ids=[859610420615446538], force_global=True)
    async def say_command(self, interaction: Interaction, str: str):
        if interaction.user.id in owners:
            await interaction.response.defer()
            await interaction.followup.send(f"{str}")

def setup(bot: commands.Bot):
    bot.add_cog(Owner(bot))
