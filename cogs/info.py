from nextcord.ext import commands
from nextcord import slash_command, Interaction
import nextcord
import time
import datetime
import platform
import psutil
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

class Info(commands.Cog):
    """Receives info commands"""
    
    @slash_command(name="botinfo",description="Show info about me",guild_ids=[794684213697052712], force_global=True)
    async def botinfo_command(interaction: Interaction):
        await interaction.response.defer()
        for guild in bot.guilds:
            mem = guild.member_count
            count =+ mem
        
        done = time.time()
        t=int(round(done - uptime_start))
        day= 86400
        hour= (t-(day*86400))/3600
        minit= (t - ((day*86400) + (hour*3600)))/60
        seconds= t - ((day*86400) + (hour*3600) + (minit*60))
        guild_url_icons = interaction.guild.icon.url
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = round(psutil.cpu_percent())
        operating_system = platform.system()
        start_time = time.time()
        msg = await interaction.followup.send("Loading info...")
        end_time = time.time()

        embed2 = nextcord.Embed(description=f"""```Name:        {bot.user}
    Bot Latency: {round(bot.latency * 1000)}ms
    Api Latency: {round((end_time - start_time) * 1000)}ms
    Runtime:     {seconds} seconds, {minit} minutes, {hour} hours, {day} days.```""", color=0xFFFFF)
        embed2.set_author(name=f"{bot.user} Information", url=botInvite, icon_url=guild_url_icons)
        embed2.add_field(name="💿 General -- Stats", value=f"""```yaml
    Servers: {len(bot.guilds)}
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



    @commands.command(brief="Shows my info", aliases = ["info", "stats", "botstats"])
    async def botinfo(self, ctx):
        for guild in bot.guilds:
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
        message = await ctx.send("Loading...")
        end_time = time.time()

        embed2 = nextcord.Embed(description=f"""```
    Name:        {bot.user}
    Bot Latency: {round(bot.latency * 1000)}ms
    Api Latency: {round((end_time - start_time) * 1000)}ms
    Runtime:     {seconds} seconds, {minit} minutes, {hour} hours, {day} days.
    ```""", color=0xFFFFF)
        embed2.set_author(name=f"{bot.user} Information", url="https://discord.com/api/oauth2/authorize?client_id=914304511236010027&permissions=902199660364562492&scope=bot%20applications.commands", icon_url=guild_url_icons)
        embed2.add_field(name="💿 General -- Stats", value=f"""```yaml
    Servers: {len(bot.guilds)}
    Users:   {count}
    ```""", inline=True)
        embed2.add_field(name="💿 Bot -- Stats", value=f"""```yaml
    Python:   {platform.python_version()}
    Nextcord: {nextcord.__version__}
    ```""", inline=True)
        embed2.add_field(name="💿 System -- Stats", value=f"""```yaml
    OS:        {operating_system}
    CPU Usage: {cpu_usage}%
    RAM Usage: {ram_usage}%
    ```""", inline=False)
        embed2.add_field(name="💿 Developer", value=f"""```yaml
    Name: AndyIsHereBoi#8909
    ID:   [683002779396079667]
    ```""", inline=False)
        embed2.add_field(name="💿 Important Links", value=f"**[Invite Link]({botInvite})・[Support Server]({supportServer})**")
        embed2.set_footer(text='Zippy Development™',icon_url=guild_url_icons)
        embed2.set_thumbnail(url=guild_url_icons)
        await message.edit("", embed=embed2)



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

            
    @slash_command(name="invite",description="Invite me to your server!",guild_ids=[859610420615446538], force_global=True)
    async def invite_command(self, interaction: Interaction):
            await interaction.response.defer()
            embed = nextcord.Embed(title="Invite me to your server!", description=f'[here]({botInvite})', color=0xEE8700)
            embed.set_footer(text=footerText)
            await interaction.followup.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(Info())

    
