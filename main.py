import os
import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands.flags import F
from nextcord import Client, Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
import datetime
import time as T
from datetime import datetime
import sys 
import asyncio
import logging
import random
import mysql.connector
from mysql.connector import Error
import traceback
replace = os.path.basename(__file__)
thing = __file__
directory = thing.replace(os.path.basename(__file__), '')
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
footerText = data['footerText']
ad_count_send = data['ad_count_send']
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command("help")
replace = os.path.basename(__file__)
thing = __file__
thing = thing.replace(os.path.basename(__file__), '')
print(directory)
directory = f"{thing}/cogs/"


mydb = mysql.connector.connect(host="207.244.233.7",                    # host address
                                user="u159_2ZQWKseyUj",                 # db username
                                password="CLKKZUg@iEJ2YiRYw!nU8o!7",    # db bassword
                                database="s159_bump-bot")               # name of database we will use          
                                    

for filename in os.listdir(directory):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded extention {filename}")
    else:
        print(f'Unable to load {filename[:-3]}')

try:
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        for (channel, message, time, serverid) in mycursor:
            print(f"{serverid}, {channel}, {message}, {time}")

except Error as e:
    print("except")
    print("Error while connecting to MySQL", e)
finally:
    print("finally")


@bot.slash_command(name="setup",description="Setup so i can be used",guild_ids=[859610420615446538], force_global=True)
async def setup_command(interaction: Interaction, message: str, channel: GuildChannel = SlashOption(channel_types=[ChannelType.text])):
    await interaction.response.defer()
    if interaction.user.id == 683002779396079667:
        mycursor.execute("INSERT INTO `server-settings`(`serverid`, `channel`, `message`, `time`) VALUES (%s, %s, %s, %s)", (interaction.guild.id, channel.id, message, round(T.time())))
        # above method prevents sql injection. MUST USE IT!!!!!
        mydb.commit()
        await interaction.followup.send(f"Tried to add GUILD ID: {interaction.guild.id}, CHANNEL ID: {channel.id}, MESSAGE: {message}, TIME: {round(T.time())}")
    else:
        await interaction.followup.send("This command is in testing.")



@bot.command(brief="This menu")
async def viewserversettings(ctx):
    mycursor.execute(f"SELECT * FROM `server-settings` WHERE serverid = {ctx.guild.id};")
    for (serverid, channel, message, time) in mycursor:
        await ctx.send(f"Ad channel: <#{channel}>, Ad message: {message}")
        if T.time() - round(int(float(time))) > 1800:
            await ctx.send("Ad time!")
            await ctx.send(str(int(float(time))))
        else:
            await ctx.send("not time")
            await ctx.send(round(int(float(time))))
            await ctx.send(T.time() - round(int(float(time))))


@bot.command()
async def deletesettings(ctx):
    mycursor.execute(f"DELETE FROM `server-settings` WHERE `serverid` = {ctx.guild.id}")
    mydb.commit()
    await ctx.send("Attempting to delete your server from the database...")


@bot.command()
async def sendads(ctx):
    await ctx.send(f"ganna send to:")
    mycursor.execute(f"SELECT * FROM `server-settings` ORDER BY RAND() LIMIT {ad_count_send};")
    for (serverid, channel, message, time) in mycursor:
        await ctx.send(f"<#{channel}>")
       

@bot.event
async def on_command_completion(ctx):
    currentDT = datetime.now()
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    channel = bot.get_channel(logchnl)
    await channel.send(f"""```[{currentDT.day}/{currentDT.month}/{currentDT.year}, {currentDT.hour}:{currentDT.minute}:{currentDT.second}]
    Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})```""")


"""
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
    else:
        print(error)
"""


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
    await chnl.send(f"Created {guild.name} in the database.")

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
        
        
@bot.command()
async def reload(ctx):
    if ctx.author.id in owners:

        replace = os.path.basename(__file__)
        thing = __file__
        thing = thing.replace(os.path.basename(__file__), '')
        directory = f"{thing}/cogs/"

        for filename in os.listdir(directory):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
                bot.load_extension(f'cogs.{filename[:-3]}')
                await ctx.send(f"Loaded {filename}")
            else:
                await ctx.send(f"Unable to load {filename}")

                
@bot.slash_command(name="reload",description="Reload the bots commands and modules",guild_ids=[859610420615446538], force_global=True)
async def reload_command(interaction: Interaction):
    if interaction.user.id in owners:
        await interaction.response.defer()

        replace = os.path.basename(__file__)
        thing = __file__
        thing = thing.replace(os.path.basename(__file__), '')
        directory = f"{thing}/cogs/"

        for filename in os.listdir(directory):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
                bot.load_extension(f'cogs.{filename[:-3]}')
                await interaction.followup.send(f"Loaded {filename}")
            else:
                await interaction.followup.send(f"Unable to load {filename}")


@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"for zb!help in {len(bot.guilds)} servers."))
    os.system("clear")
    print(f"I\'m in {bot.user}")
    mycursor.execute(f"SELECT * FROM `server-settings` WHERE serverid = 859610420615446538;")
    for (serverid, channel, message, time) in mycursor:
        print(f"Server ID: {serverid}, Ad channel: {channel}, Ad message: {message}, Last advertised at: {time}")


@bot.command(brief="This menu")
async def help(ctx):
    global msg
    msg = await ctx.send('Select help menus:', view=Helpbutton())


@bot.slash_command(name="help",description="Show my commands",guild_ids=[859610420615446538], force_global=True)
async def help_command(interaction: Interaction):
    await interaction.response.defer()
    await interaction.followup.send("Click the buttons below.", view=Helpbutton())


class Helpbutton(nextcord.ui.View):
    @nextcord.ui.button(label='Bump', style=nextcord.ButtonStyle.green)
    async def one(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Bump Commands", description="""`bump` - Bumps your server to a few random others.
`setup` - Setup your bump channels.""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)
                
    @nextcord.ui.button(label='Info', style=nextcord.ButtonStyle.green)
    async def two(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Bump Commands", description="""`botinfo` - Show info about the bot
`ping` - Show the bots ping
`serverinfo` - Info of the current server
`invite` - My invite link""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)

    @nextcord.ui.button(label='Staff', style=nextcord.ButtonStyle.green)
    async def three(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Bump Commands", description="""`purge` - Purge messages in the current channel
`activity` - Change the bots custom status
`status` - Change status (online/idle/dnd)""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)

    @nextcord.ui.button(label='Other', style=nextcord.ButtonStyle.green)
    async def four(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = bot.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(interaction.message.id)
        embed = nextcord.Embed(title=f"Uncategorized Commands", description="""`help` - This message""", color=0xFFFFF)
        embed.set_footer(text=footerText)
        await msg.edit("", embed=embed)

bot.run(token)
# made by AndyIsHereBoi#8909
