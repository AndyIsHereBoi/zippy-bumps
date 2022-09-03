import os
import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands.flags import F
from nextcord import Client, Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
import datetime
import time
from datetime import datetime
import sys
import asyncio
import logging
import random
import mysql.connector
from mysql.connector import Error


"""
logger2 = logging.getLogger("nextcord.client")
logger3 = logging.getLogger("nextcord.state")
LOGGING_FORMAT = "[{asctime}][{filename}][{lineno:3}][{funcName}][{levelname}] {message}"
log_format = logging.Formatter(LOGGING_FORMAT, style="{")
log_console_handler = logging.StreamHandler(sys.stdout)
log_console_handler.setFormatter(log_format)
logger2.addHandler(log_console_handler)
logger2.setLevel(logging.DEBUG)
logger3.addHandler(log_console_handler)
logger3.setLevel(logging.DEBUG)
"""

import json
config_file = "config.json"
with open("config.json") as config_file:
    data = json.load(config_file)

owners = data['owners']
token = data['token']
prefix = data['prefix']
logchnl = data['logchannel']
supportServer = data['supportServer']
botInvite = data['botInvite']
footerText = data['footerText']
ad_count_send = data['ad_count_send']


bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command("help")


replace = os.path.basename(__file__)
thing = __file__
thing = thing.replace(os.path.basename(__file__), '')
print(thing)
print(thing)
print(thing)
directory = f"{thing}/cogs/"
print(directory)
print(directory)
print(__file__)

for filename in os.listdir(directory):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded extention {filename}")
    else:
        print(f'Unable to load {filename[:-3]}')

try:
    mydb = mysql.connector.connect(host="207.244.233.7:3306",
                                    user="u159_2ZQWKseyUj", 
                                    password="CLKKZUg@iEJ2YiRYw!nU8o!7", 
                                    database="server-settings")
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        mycursor = mydb.cursor()
except Error as e:
    print("except")
    print("Error while connecting to MySQL", e)
finally:
    print("finally")

@bot.command()
async def dbset(ctx, value):
    await ctx.send(f"attempting to set {value} in the db")
    

                                 
                 
class Helpbutton(nextcord.ui.View):
    @nextcord.ui.button(label='Bump', style=nextcord.ButtonStyle.green)
    async def one(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Bump Commands", description="""`bump` - Bumps your server to a few random others.
`setup` - Setup your bump channels.
""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)
                
    @nextcord.ui.button(label='Info', style=nextcord.ButtonStyle.green)
    async def two(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Bump Commands", description="""
        `botinfo` - Show info about the bot
`ping` - Show the bots ping
`serverinfo` - Info of the current server
`invite` - My invite link
""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)

    @nextcord.ui.button(label='Staff', style=nextcord.ButtonStyle.green)
    async def three(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Bump Commands", description=
"""
`purge` - Purge messages in the current channel
`activity` - Change the bots custom status
`status` - Change status (online/idle/dnd)
""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)

    @nextcord.ui.button(label='Other', style=nextcord.ButtonStyle.green)
    async def four(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Uncategorized Commands", description=
"""
`help` - This message
""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)
                        
                        
                        
                        
                        
@bot.event 
async def on_ready():
    os.system("clear")
    print(f"I\'m in {bot.user}")
    if not hasattr(bot, "uptime_start"):
        global uptime_start
        uptime_start = time.time()
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"for zb!help in {len(bot.guilds)} servers."))
    


@bot.command(brief="Invite me!")
async def invite(ctx):
        embed = nextcord.Embed(title="Invite me to your server!", description=f'[here]({botInvite})', color=0xEE8700)
        embed.set_footer(text=footerText)
        await ctx.send(embed=embed)


@bot.command(brief="Info about the current server")
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

@bot.command(brief="This menu")
async def help(ctx):
    global msg
    msg = await ctx.send('Select help menus:', view=Helpbutton())

                
        
                
@bot.event
async def on_command_completion(ctx):
    currentDT = datetime.now()
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    channel = bot.get_channel(logchnl)
    await channel.send(f"""```[{currentDT.day}/{currentDT.month}/{currentDT.year}, {currentDT.hour}:{currentDT.minute}:{currentDT.second}]
    Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})```""")
        
        
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Do `"    +prefix + "help`")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing a required argument.    Do `" + prefix + "help`")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the correct permissions to run this command.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have sufficient permissions!")
        
@bot.event
async def on_guild_join(guild):
    chnl = bot.get_channel(921733527496687616)
    embed = nextcord.Embed(title=f"I joined {guild.name}", description="Info below.", color=0xFFFFF)
    embed.add_field(name="Guild ID", value=str(guild.id), inline=True)
    embed.add_field(name="Guild Member Count", value=str(guild.member_count), inline=True)
    embed.add_field(name="Guild Server Owner", value=str(guild.owner), inline=True)
    embed.add_field(name="Guild Nitro Boosts", value=str(guild.premium_subscription_count), inline=True)
    embed.add_field(name="Guild Description", value=str(guild.description), inline=True)
    embed.set_footer(text=footerText)
    await chnl.send(embed = embed)
        
@bot.event
async def on_guild_remove(guild):
    chnl = bot.get_channel(921733528360726558)
    embed = nextcord.Embed(title=f"I left {guild.name}", description="Info below.", color=0xFFFFF)
    embed.add_field(name="Guild ID", value=str(guild.id), inline=True)
    embed.add_field(name="Guild Member Count", value=str(guild.member_count), inline=True)
    embed.add_field(name="Guild Server Owner", value=str(guild.owner), inline=True)
    embed.add_field(name="Guild Nitro Boosts", value=str(guild.premium_subscription_count), inline=True)
    embed.add_field(name="Guild Description", value=str(guild.description), inline=True)
    embed.set_footer(text=footerText)
    await chnl.send(embed = embed)

@bot.slash_command(name="help",description="Show my commands",guild_ids=[859610420615446538], force_global=True)
async def help_command(interaction: Interaction):
        await interaction.response.defer()
        await interaction.followup.send("Click the buttons below.", view=Helpbutton())
        



@bot.command()
async def load(ctx,cog):
    await ctx.send(f"loading {cog}...")
    bot.load_extension(cog)

@bot.command()
async def unload(ctx,cog):
    await ctx.send(f"unloading {cog}...")
    bot.unload_extension(cog)

@bot.command()
async def reload(ctx,cog):
    bot.unload_extension(cog)
    await ctx.send(f"unloading {cog}...")
    bot.load_extension(cog)
    await ctx.send(f"loading {cog}...")

bot.run(token)