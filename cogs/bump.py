import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands.flags import F
from nextcord import Client, Interaction, SlashOption, ChannelType, Message, slash_command
from nextcord.abc import GuildChannel
import time
import os
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
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @slash_command(name="bump",description="Bump your servers!",guild_ids=[859610420615446538], force_global=True)
    async def bump_command(self, interaction: Interaction):
        await interaction.response.defer()
        
        await interaction.followup.send("exmaple")



def setup(bot: commands.Bot):
    bot.add_cog(Bump(bot))
