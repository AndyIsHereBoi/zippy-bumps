from nextcord.ext import commands
from nextcord import slash_command, Interaction
import nextcord
import time
import datetime
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
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command("help")
footerText = data['footerText']
ad_count_send = data['ad_count_send']


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

class Owner(commands.Cog):
    """Receives owner commands"""
    
    @slash_command(name="ping",description="Bot latency",guild_ids=[794684213697052712], force_global=True)
    async def ping_command(interaction: Interaction):
        await interaction.response.defer()
        start_time = time.time()
        msg = await interaction.followup.send("Testing Ping...")
        end_time = time.time()
        await msg.edit(content=f"Pong!\nBot latency: {round(bot.latency * 1000)}ms\nAPI latency: {round((end_time - start_time) * 1000)}ms")
    
    @commands.command()
    async def ping(ctx):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()
        await message.edit(content=f"Pong!\nAPI there: {round(bot.latency * 1000)}ms\nAPI there and back: {round((end_time - start_time) * 1000)}ms")
    

    @slash_command(name="status",description="Change my status",guild_ids=[794684213697052712], force_global=True)
    async def status_command(interaction: Interaction, choice: str = SlashOption(name="type", description="Online, Idle, DND, Offline", choices={"Online": "Online", "Idle": "Idle","DND": "DND"})):
        await interaction.response.defer()
        if interaction.user.id in owners:
            if choice == "Online":
                await interaction.followup.send("Set status to Online")
                await bot.change_presence(status=nextcord.Status.online)
            if choice == "Idle":
                await interaction.followup.send("Set status to Idle")
                await bot.change_presence(status=nextcord.Status.idle)
            if choice == "DND":
                await interaction.followup.send("Set status to DND")
                await bot.change_presence(status=nextcord.Status.dnd)
        else:
            await interaction.followup.send("You must be a owner to perform this action.")

    @commands.command()
    async def status(ctx):
        if ctx.author.id in owners:
            await ctx.send('Select bot status:', view=Status())


    @commands.command(brief="[Owner Only] Set the bots watching activity")
    async def activity(ctx, activity):
        if ctx.author.id in owners:
            await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=activity))
                    
                    
    
    @commands.command(brief="[Owner Only] Delete messages")
    async def purge(ctx, ammount):
        if ctx.author.id in owners:
            ammount = int(ammount)
            if ammount > 100:
                await ctx.send("You can not purge more then 100 messages at a time.")
            elif ammount < 1:
                await ctx.send("You need to purge more then 0 messages.")
            else:
                ammount = int(ammount)
                await ctx.channel.purge(limit=ammount)


def setup(bot: commands.Bot):
    bot.add_cog(Owner())
