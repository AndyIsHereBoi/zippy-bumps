import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands.flags import F
from nextcord import Client, Interaction, SlashOption, ChannelType, Message, slash_command
from nextcord.abc import GuildChannel
import time
import datetime
import platform
import psutil
import sys
import asyncio
import os
import logging
import random
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


class Info(commands.Cog):
    """Receives info commands"""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.Cog.listener()
    async def on_ready(self):
        if not hasattr(bot, "uptime_start"):
            global uptime_start
            uptime_start = time.time()


    
    
    @slash_command(name="botinfo",description="Show info about me",guild_ids=[794684213697052712], force_global=True)
    async def botinfo_command(self, interaction: Interaction):
        await interaction.response.defer()
        for guild in self.bot.guilds:
            mem = guild.member_count
            count =+ mem
        
        done = time.time()
        t=int(round(done - uptime_start))
        day= t//86400
        hour= (t-(day*86400))//3600
        minit= (t - ((day*86400) + (hour*3600)))//60
        seconds= t - ((day*86400) + (hour*3600) + (minit*60))
        guild_url_icons = interaction.guild.icon.url
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = round(psutil.cpu_percent())
        operating_system = platform.system()
        start_time = time.time()
        msg = await interaction.followup.send("Loading info...")
        end_time = time.time()

        embed2 = nextcord.Embed(description=f"""```
Name:        {self.bot.user}
Bot Latency: {round(self.bot.latency * 1000)}ms
Api Latency: {round((end_time - start_time) * 1000)}ms
Runtime:     {seconds} seconds, {minit} minutes, {hour} hours, {day} days.```""", color=0xFFFFF)
        embed2.set_author(name=f"{self.bot.user} Information", url=botInvite, icon_url=guild_url_icons)
        embed2.add_field(name="💿 General -- Stats", value=f"""```yaml
Servers:   {len(self.bot.guilds)}
Users:     {count}```""", inline=True)
        embed2.add_field(name="💿 Bot -- Stats", value=f"""```yaml
Python:    {platform.python_version()}
Nextcord:  {nextcord.__version__}```""", inline=True)
        embed2.add_field(name="💿 System -- Stats", value=f"""```yaml
OS:        {operating_system}
CPU Usage: {cpu_usage}%
RAM Usage: {ram_usage}%```""", inline=False)
        embed2.add_field(name="💿 Developer", value=f"""```yaml
Name: AndyIsHereBoi#8909
ID:   [683002779396079667]```""", inline=False)
        embed2.add_field(name="💿 Important Links", value=f"**[Invite Link]({botInvite})・[Support Server]({supportServer})**")
        embed2.set_footer(text='Zippy Development™',icon_url=guild_url_icons)
        await msg.edit("", embed=embed2)


    @commands.command(brief="Shows my info", aliases = ["info", "stats", "botstats"])
    async def botinfo(self, ctx):
        for guild in self.bot.guilds:
            mem = guild.member_count
            count =+ mem
        
        done = time.time()
        t=int(round(done - uptime_start))
        day= t//86400
        hour= (t-(day*86400))//3600
        minit= (t - ((day*86400) + (hour*3600)))//60
        seconds= t - ((day*86400) + (hour*3600) + (minit*60))
        guild_url_icons = ctx.guild.icon.url
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = round(psutil.cpu_percent())
        operating_system = platform.system()
        start_time = time.time()
        msg = await ctx.send("Loading...")
        end_time = time.time()

        embed2 = nextcord.Embed(description=f"""```
Name:        {self.bot.user}
Bot Latency: {round(self.bot.latency * 1000)}ms
Api Latency: {round((end_time - start_time) * 1000)}ms
Runtime:     {seconds} seconds, {minit} minutes, {hour} hours, {day} days.```""", color=0xFFFFF)
        embed2.set_author(name=f"{self.bot.user} Information", url=botInvite, icon_url=guild_url_icons)
        embed2.add_field(name="💿 General -- Stats", value=f"""```yaml
Servers: {len(self.bot.guilds)}
Users:   {count}```""", inline=True)
        embed2.add_field(name="💿 Bot -- Stats", value=f"""```yaml
Python:   {platform.python_version()}
Nextcord: {nextcord.__version__}```""", inline=True)
        embed2.add_field(name="💿 System -- Stats", value=f"""```yaml
OS:        {operating_system}
CPU Usage: {cpu_usage}%
RAM Usage: {ram_usage}%```""", inline=False)
        embed2.add_field(name="💿 Developer", value=f"""```yaml
Name: AndyIsHereBoi#8909
ID:   [683002779396079667]```""", inline=False)
        embed2.add_field(name="💿 Important Links", value=f"**[Invite Link]({botInvite})・[Support Server]({supportServer})**")
        embed2.set_footer(text='Zippy Development™',icon_url=guild_url_icons)
        await msg.edit("", embed=embed2)

    @commands.command(brief="Info about the current server")
    async def serverinfo(ctx):
        embed = nextcord.Embed(title=f"{ctx.guild.name}'s info'", description="", color=0xFFFFF)
        embed.add_field(name="Member Count", value=str(ctx.guild.member_count), inline=True)
        embed.add_field(name="Rules Channel", value=str(ctx.guild.rules_channel), inline=True)
        embed.add_field(name="Server Owner:", value=str(ctx.guild.owner), inline=True)
        embed.add_field(name="Verification Level", value=str(ctx.guild.verification_level), inline=True)
        embed.add_field(name="AFK Channel", value=str(ctx.guild.afk_channel), inline=True)
        embed.add_field(name="AFK Timeout (in seconds)", value=str(ctx.guild.afk_timeout), inline=True)
        embed.add_field(name="Guild Description", value=str(ctx.guild.description), inline=True)
        embed.add_field(name="Nitro Boosts", value=str(ctx.guild.premium_subscription_count), inline=True)
        embed.add_field(name="System Messages Channel", value=str(ctx.guild.system_channel), inline=True)
        embed.add_field(name="Server Booster Role", value=str(ctx.guild.premium_subscriber_role), inline=True)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=footerText)
        await ctx.send(embed=embed)


    @slash_command(name="serverinfo",description="Show info of the current server",guild_ids=[794684213697052712], force_global=True) # id is build dream project server
    async def serverinfo_command(self, interaction: Interaction):
            await interaction.response.defer()
            embed = nextcord.Embed(title=f"{interaction.guild.name}'s info'", description="", color=0xFFFFF)
            embed.add_field(name="Member Count", value=str(interaction.guild.member_count), inline=True)
            embed.add_field(name="Rules Channel", value=str(interaction.guild.rules_channel), inline=True)
            embed.add_field(name="Verification Level", value=str(interaction.guild.verification_level), inline=True)
            embed.add_field(name="AFK Channel", value=str(interaction.guild.afk_channel), inline=True)
            embed.add_field(name="AFK Timeout (in seconds)", value=str(interaction.guild.afk_timeout), inline=True)
            embed.add_field(name="Guild Description", value=str(interaction.guild.description), inline=True)
            embed.add_field(name="Nitro Boosts", value=str(interaction.guild.premium_subscription_count), inline=True)
            embed.add_field(name="System Messages Channel", value=str(interaction.guild.system_channel), inline=True)
            embed.add_field(name="Server Booster Role", value=str(interaction.guild.premium_subscriber_role), inline=True)
            embed.set_thumbnail(url=interaction.guild.icon.url)
            embed.set_footer(text=footerText)
            await interaction.followup.send(embed=embed)

            
    @commands.command(brief="Invite me!")
    async def invite(ctx):
        embed = nextcord.Embed(title="Invite me to your server!", description=f'[here]({botInvite})', color=0xEE8700)
        embed.set_footer(text=footerText)
        await ctx.send(embed=embed)

    @slash_command(name="invite",description="Invite me to your server!",guild_ids=[859610420615446538], force_global=True)
    async def invite_command(self, interaction: Interaction):
            await interaction.response.defer()
            embed = nextcord.Embed(title="Invite me to your server!", description=f'[here]({botInvite})', color=0xEE8700)
            embed.set_footer(text=footerText)
            await interaction.followup.send(embed=embed)

    @slash_command(name="ping",description="Bot latency",guild_ids=[794684213697052712], force_global=True)
    async def ping_command(self, interaction: Interaction):
        await interaction.response.defer()
        start_time = time.time()
        msg = await interaction.followup.send("Testing Ping...")        
        end_time = time.time()
        await msg.edit(content=f"Pong!\nBot latency: {round(self.bot.latency * 1000)}ms\nAPI latency: {round((end_time - start_time) * 1000)}ms")
    
    @commands.command()
    async def ping(self, ctx):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()
        await message.edit(content=f"Pong!\nAPI there: {round(self.bot.latency * 1000)}ms\nAPI there and back: {round((end_time - start_time) * 1000)}ms")
    

def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))
