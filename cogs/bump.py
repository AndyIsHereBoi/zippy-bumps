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


class Bump(commands.Cog):
    """Receives bump commands"""
    
    @slash_command(name="bump",description="Bump your servers!",guild_ids=[859610420615446538], force_global=True)
    async def bump_command(interaction: Interaction):
        await interaction.response.defer()
        
        await interaction.followup.send("I cannot find the `#zb-bump` channel. You must have it to post ads, and recieve ads.")



def setup(bot: commands.Bot):
    bot.add_cog(Bump())
