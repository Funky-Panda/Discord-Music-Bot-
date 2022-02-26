import os
from datetime import datetime
import discord
from discord.ext import commands
import random
from webserver import keep_alive
from discord import FFmpegPCMAudio
from discord.utils import get
from youtube_dl import YoutubeDL
import asyncio
#from discord_buttons_plugin import *
from discord_slash import SlashCommand
#pip install -U discord-py-slash-command

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(commands.when_mentioned_or("."),case_insensitive=True,intents=intents)
#buttons = ButtonsClient(client)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    #while True:
    #  print("txt was cleared")
    #  await asyncio.sleep(20)
    #  with open("spam_detect.txt","r+") as file:
    #    file.truncate(0)
    await client.change_presence(activity=discord.Game(name="MILK |  /help"))
    print(r"""\

                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /

                Milk is online!
            """)
    

@client.event
async def on_message(message):
  if str(message.channel) ==  "r-u-l-e-s" and message.content != "":
    await message.channel.purge(limit=1)
    
#@client.event
#async def on_message(message):
#  counter = 0
#  with open("spam_detect.txt","r+") as file:
#    for lines in file:
#      if lines.strip("\n") == str(message.author.id):
#        counter+=1

#    file.writelines(f"{str(message.author.id)}\n")
#    if counter >8:
#      await message.author.send(f"You have been removed from: **{message.guild.name}** for Spamming\n You can join back but don't do this again: https://discord.gg/Dc8pUvbcpF")
#      print("Person banned")
#      await message.guild.ban(message.author,reason="For Spamming")
#      await asyncio.sleep(1)
#      await message.guild.unban(message.author)
 #     await message.channel.send(f"{message.author.mention} Has been banned for Spamming")



@slash.slash(description="This will give you access to the server")
async def verify(ctx):
  role = discord.utils.get(ctx.guild.roles,name="Green Cap🟢")
  await ctx.author.add_roles(role)
  await ctx.send(f"{ctx.author.mention} has been verified")
  await ctx.author.send(f"{ctx.author.mention} has been verified")

@verify.error
async def verify(ctx, error):
    if isinstance(error, commands.Forbidden):
          await ctx.send(f"{ctx.author.mention} does not have administrator.")
    

@slash.slash(description="This will display Commands for you to use")
@commands.has_role("Green Cap🟢")
async def help(ctx):
    embed = discord.Embed(
      title = "MILK",
      description = "List of commands:",
      color = discord.Color.blue()
    )
    embed.add_field(name="/admin",value="This will display commands that can only be used by administrators", inline=False)
    embed.add_field(name="/whois @(user)",value="This will display info about discord profile", inline=False)
    embed.add_field(name="/link",value="This will give you the link to the server.",inline=False)
    embed.add_field(name="/serverinfo",value="This will give you info about this server.")
    embed.add_field(name="/dm",value="This will dm you some STEVEN pics", inline=False)
    embed.add_field(name="/poll (what you want to poll to be called)",value="This will make a poll", inline=False)
    embed.add_field(name="/givenum",value="This will let you use a random number generator", inline=False)
    embed.add_field(name="/sing",value="Albin will sing for you", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command(name="dfasdfasdfafadfaf")
@commands.has_role("Green Cap🟢")
async def link(ctx):
  await ctx.message.delete()
  msg = "https://discord.gg/CeuVvJNGxf\nThis message will delete in"
  ##message = await ctx.send("hello")
  ##await asyncio.sleep(1)
  ##await message.edit(content="newcontent")
  message = await ctx.send(msg+" 10",delete_after=11)
  await asyncio.sleep(1)
  await message.edit(content=msg+" 9")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 8")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 7")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 6")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 5")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 4")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 3")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 2")
  await asyncio.sleep(1)
  await message.edit(content=msg+" 1")


# THIS IS THE RULES FOR MILK!
@client.command(name="rule")
@commands.has_role("Green Cap🟢")
async def rule(ctx):
  
    embed = discord.Embed(
      title = "Rules",
      description = "List of Rules:",
      color = discord.Color.blue()
    )
    embed.add_field(name=dash,value="***1.*** You must respect all users, regardless of your liking towards them.\n    Treat others the way you want to be treated.",inline=False)
    embed.add_field(name=dash,value="***2.*** The use of profanity should be kept to a minimum. However, any\n derogatory language towards any user is prohibited.",inline=False)
    embed.add_field(name=dash,value="***3.*** Don't send a lot of small messages right after each other. Do not\n disrupt chat by spamming.",inline=False)
    embed.add_field(name=dash,value="***4.*** Raiding or mentions of raiding are not allowed.",inline=False)
    embed.add_field(name=dash,value="***5.*** Threats to other users of DDoS, Death, DoX, abuse, and other\n malicious threats are absolutely prohibited and disallowed.",inline=False)
    embed.add_field(name=dash,value="For more visit: https://discordapp.com/guidelines",inline=False)
    embed.set_footer(text="NOTE: This was copied and pasted", icon_url="https://images-ext-1.discordapp.net/external/kUMY0h5lWHV5_lmM14oWg5N-w9C24-me292dkz1jbi0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/891456975924240456/b374934c5d3d7ede833dd23fd14bcb25.webp?width=647&height=647")
    message_channel = client.get_channel(897555271759577129)
    await message_channel.send(embed=embed)

@client.command(name="send")
@commands.has_role("GOD")
async def send(ctx):
    message_channel = client.get_channel(897555271759577129)
    await message_channel.send("> To gain perms: `/verify`")

@client.command(aliases=["ms", "aliases!"]) # You make make the command respond to other commands too
async def ping(ctx): # a_variable is a parameter you use in the command
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@slash.slash(description="This Is A List of Commands For The Music:")
@commands.has_role("Green Cap🟢")
async def musichelp(ctx):
    embed = discord.Embed(title = "STEVEN 🎶", description = "List of commands:",color = discord.Color.blue())
    embed.add_field(name="/join",value="This will make the bot join your vc you are in.", inline=False)
    embed.add_field(name="/play (Youtube-Link)",value="This play the youtube audio.", inline=False)
    embed.add_field(name="/pause",value="This pause the music audio.", inline=False)
    embed.add_field(name="/resume",value="This will resume the audio.", inline=False)
    embed.add_field(name="/stop",value="This will restart the music if any issues.", inline=False)
    embed.add_field(name="/leave or .disconnect",value="This will kick the bot from the vc the bot is in.", inline=False)
    await ctx.send(embed=embed)




@slash.slash(description="This Will Let You Make a poll.")
@commands.has_role("Green Cap🟢")
async def poll(ctx,*,message):
  embed=discord.Embed(title=f"{message}")
  embed.set_footer(text=f"Request by - {ctx.author}")
  msg = await ctx.send(embed=embed)
  await msg.add_reaction("✅")
  await msg.add_reaction("❌")

@slash.slash(description="This will DM you.")
@commands.has_role("Green Cap🟢")
async def dm(ctx):
    await ctx.send(random.choice(fromservermessages))
    await ctx.author.send(random.choice(dmmessages))
    await ctx.author.send(random.choice(images))
dmmessages = [
"Fuck of you creep.",
"Fucking hell why are you asking for photos of little boys.",
"Bruh fuck you.\n you ain't getting any pictures",
"Your wish is my command \n Sike I was lying",
"Wow you wanna see little kid your kinda weird"
]

dash = "----------------------------------------------------------------------------------"

fromservermessages = [
  "You have been sent a message.",
  "The message has been sent",
  """I have DM'ed you""",
  "You have been messsaged"
]


@slash.slash(description="This Will Clear Messages")
@commands.has_permissions(administrator=True)
#@commands.has_role("Secrete")
async def clear(ctx, limit: int):
  embed=discord.Embed(title="Cleared Messages",description=f"{ctx.author.mention} Cleared **{limit}** Messages")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894709014280142908/897541185764221009/discord_milk_small.png")
  msg = "This Message Will Delete in: 10 Seconds"
  embed.set_footer(text=msg, icon_url=ctx.author.avatar_url)
  await ctx.channel.purge(limit=limit)
  await ctx.send(embed=embed,delete_after=10)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.author.mention} does not have administrator.")
    #if isinstance(error, commands.MissingRole):
    #      await ctx.send(f"You do not have permistion to use this only <@471639809962672129> does.")

@slash.slash(description="List of Admin Commands:")
@commands.has_permissions(administrator=True)
async def admin(ctx):
    embed = discord.Embed(title = "Administrator", description = "List of commands:",color = discord.Color.blue())
    embed.add_field(name="/clear (the amount you want to clear)",value="This will delete messages", inline=False)
    embed.add_field(name="/kick (@user)",value="This will kick the user from the server", inline=False)
    embed.add_field(name="/ban (@user)",value="This will ban the user from the server", inline=False)
    embed.add_field(name="/albin",value="This can only be used by <@471639809962672129>", inline=False)
    embed.add_field(name="/lewis",value="This share a video of lewis getting raped", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@admin.error
async def admin_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.author.mention} does not have administrator.")

@slash.slash(description=f"Albins amazing singing")
async def sing(Context):
    channel = Context.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("singing.mp3")
    player = voice.play(source)
    await asyncio.sleep(6)
    await Context.voice_client.disconnect()

@slash.slash(description=f"This Can Only Be used By FunkyPanda#8662")
@commands.has_role("z")
async def albin(Context):
    channel = Context.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("albin-n_word.mp3")
    player = voice.play(source)
    await asyncio.sleep(4)
    await Context.voice_client.disconnect()


@albin.error
async def albin_error(ctx, error):
    if isinstance(error, commands.MissingRole):
          await ctx.send(f"You do not have permistion to use this only <@471639809962672129> does.")



@slash.slash(description="Send you funny video.")
@commands.has_permissions(administrator=True)
async def lewis(ctx):
  await ctx.send(file=discord.File('lewis.mov'))

@lewis.error
async def lewis_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.author.mention} does not have administrator.")

@slash.slash(description="This Will Kick a user from the server")
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'{member.mention} has been kicked for {reason}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.author.mention} does not have administrator.")


@slash.slash(description="Ban a user from the server")
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned for {reason}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.author.mention} does not have administrator.")


@client.event
async def on_member_join(member):
    embed=discord.Embed(title=f"Welcome {member.name} 👋", description=f"Enjoy your stay at {member.guild.name}!")
    embed.set_thumbnail(url=member.avatar_url)
    #role = get(member.guild.roles, id=896349719381569546)
    #await member.add_roles(role)
    guild = member.guild
    if guild.system_channel is not None:
        #msg = f"Welcome {member.mention} to {guild.name}  🎉🎉"
        await guild.system_channel.send(embed = embed)

@client.command(pass_context = True)
async def timedate(ctx):
  embed = discord.Embed(title = "Date", description = (Date),color = (0x552E12))
  embed.add_field(name="Time",value=(Time))
  await ctx.send(embed=embed)

today = datetime.today()
now = datetime.now()
Date = today.strftime("%d %B, %Y")
Time = now.strftime("%H:%M")

@slash.slash(description="Display Server Infomation")
@commands.has_role("Green Cap🟢")
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  #description = str(ctx.guild.description)
  region = str(ctx.guild.region)
  icon = str(ctx.guild.icon_url)
   
  #role = ctx.guild.get_role(893618557370392576)
#for member in role.members:
    #await ctx.send(member.mention)

  embed = discord.Embed(
      title=name + " Server Information",
      description=f"Milk Bot was coded by <@471639809962672129>",
      #color=discord.Color.blue()
      color = (0xa891d7)
    )
  #role = discord.utils.get(ctx.message.server.roles, name="ARE LORD")
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner:", value=ctx.guild.owner.display_name,inline=False)
  #embed.add_field(name="ARE LORD:", value=(role))
  #embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=False)
  #embed.add_field(name="Member Count", value=memberCount, inline=True)
  embed.add_field(name="Roles:", value=len(ctx.guild.roles),inline=False)
  #embed.add_field(name="Booster Staus:", value=ctx.guild.premium_subscription_count,inline=False)
  embed.add_field(name="Member Count:", value=ctx.guild.member_count,inline=False)
  embed.add_field(name="Channels:", value=len(ctx.guild.channels),inline=False)
  embed.add_field(name="Created:", value=ctx.guild.created_at.strftime("%d %B, %Y"),inline=False)
  #embed.add_field(name="Owner:", value=ctx.guild.owner.display_name)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  await ctx.send(embed=embed)

@slash.slash(description="Info On A User")
@commands.has_role("Green Cap🟢")
async def whois(ctx,user:discord.Member=None):
  roles = " ".join([role.mention for role in user.roles])
  embed = discord.Embed(color=user.color)
  embed.set_author(name=f"user Info - {user}"),
  embed.set_thumbnail(url=user.avatar_url),
  icon_url = ctx.author.avatar_url
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url),
  #embed.add_field(name="ID:",value=user.id,inline=False)
  embed.add_field(name="Nickname:",value=user.display_name,inline=False)
  embed.add_field(name="Created Account:",value=user.created_at.strftime("%d %B, %Y"),inline=False)
  embed.add_field(name="Joined server:",value=user.joined_at.strftime("%d %B, %Y"),inline=False)
  embed.add_field(name="Bot?",value=user.bot,inline=False)
  embed.add_field(name="Roles:", value=f"{roles}", inline=False)
  await ctx.send(embed=embed)



#######################################################RANDOM NUMBER GEN####################
@slash.slash(description="Random Number Gen")
@commands.has_role("Green Cap🟢")
async def givenum(ctx):

    # checks the author is responding in the same channel
    # and the message is able to be converted to a positive int
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("Type a number")
    msg1 = await client.wait_for("message", check=check)
    await ctx.send("Type a second, larger number")
    msg2 = await client.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        await ctx.send(f"You got {value}.")
    else:
        await ctx.send(":warning: Please ensure the first number is smaller than the second number:warning:")

########################################################ALFIE GAMER#######################################


@client.command(pass_context = True)
async def test(ctx):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("Hold up ring ding.mp3")
    player = voice.play(source)


#@client.command()
#async def join(ctx):
#    if (ctx.author.voice): # If the person is in a channel
#        channel = ctx.author.voice.channel
 #       await channel.connect()
 #       await ctx.send('Bot joined')
 #   else:
 #       await ctx.send("You must be in a voice channel first so I can join it.")
#
@slash.slash(description="Make The Bot Leave Your Vc.")
@commands.has_role("Green Cap🟢")
async def leave(context):
        channel = context.author.voice.channel
        await context.voice_client.disconnect()
        await context.send(f"The bot has left {channel}")

@slash.slash(description="Make The Bot Leave Your Vc.")
@commands.has_role("Green Cap🟢")
async def disconnect(context):
        channel = context.author.voice.channel
        await context.voice_client.disconnect()
        await context.send(f"The bot has left {channel}")

  

#@tasks.loop(seconds=1)
#async def called_once_a_day():
#    message_channel = client.get_channel(target_channel_id)
#    print(f"Got channel {message_channel}")
#    await message_channel.send("https://cdn.discordapp.com/attachments/796750832305307719/891800949180477540/89941357-bad-santa-claus-in-snow-flakes-sunglasses-grab-young-long-legs-show-middle-finger-sign-new-.png")
#    await message_channel.send("https://cdn.discordapp.com/attachments/796750832305307719/891801503365472276/images.png")

#@called_once_a_day.before_loop
#async def before():
#    await client.wait_until_ready()
#    print("Finished waiting")


#@client.command()
#async def nothing(ctx):
#    await ctx.send("This Is Nothing.")
#    await ctx.send(called_once_a_day.start())


images = ["https://cdn.discordapp.com/attachments/887367307612020796/893589108578979840/artworks-000127888315-p1zyoc-t500x500.png","https://cdn.discordapp.com/attachments/887367307612020796/893589261088092170/2566818_0.png","https://cdn.discordapp.com/attachments/887367307612020796/893589388162891806/Fuck-you-Cartoon-Car-Sticker-Decor-Removable-Black-silver-CL509.png"]

@slash.slash(name='join', description='Tells the bot to join the voice channel')
@commands.has_role("Green Cap🟢")
async def join(Context):
    channel = Context.author.voice.channel
    await channel.connect()
    await Context.send(f"The Bot Has Joined {channel}")


@client.command()
async def ask(ctx):

        _list = [
        "when was I Born?", 
        '9 + 10']

        list1 = random.choice(_list)

        def answer():
            answer = "-1"
            if _list[0] == list1:
                answer = "1 July 2006"
            else: 
                answer = "2"
            return answer

        await ctx.send("What is the answer to this question?")
        await asyncio.sleep(1)
        await ctx.send(list1)
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        msg = await client.wait_for('message', check=check, timeout=None)

        if msg.content == answer():
            await ctx.send("good")
        else:
            await ctx.send("no")   



@slash.slash(description="Make The Bot Play Any Youtube Video.")
@commands.has_role("Green Cap🟢")
async def play(Context, url):
    YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True','default_search': 'auto', 'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s','audioformat': 'mp3','nocheckcertificate': True,'ignoreerrors': False,'logtostderr': False,'quiet': True,'no_warnings': True,}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=Context.guild)
    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url , download=False)
            info_dict = ydl.extract_info(url, download=False)
        URL = info['url']
        title = info['title']
        uploader = info['uploader']
        print(f"The video: {title} is being downloaded")
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await Context.send(f'Bot is now playing: **{title}** 🎵  \nBy: **{uploader}**')
        print(f"The video: {title} is now downloaded")

 
    else:
        await Context.send(f"Bot is already playing: **{title}**")
        return

#@play.error
#async def play_error(ctx, error):
#    if isinstance(error, commands.CommandInvokeError):
#      channel = ctx.author.voice.channel
#      await channel.connect()

#video = "youtube.com/watch?v=1liVAQdAEKA"
#YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True','default_search': 'auto', 'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s','audioformat': 'mp3','nocheckcertificate': True,'ignoreerrors': False,'logtostderr': False,'quiet': True,'no_warnings': True,}
#with YoutubeDL(YDL_OPTIONS) as ydl:
#      info_dict = ydl.extract_info(video, download=False)
#      video_url = info_dict.get("url", None)
#      video_id = info_dict.get("id", None)
 #     video_title = info_dict.get('title', None)
  #    print(video_title)


#@client.command()
#async def data(ctx):
#  requester = ctx.author
#  self.channel = ctx.channel
#  self.data = data
#  self.uploader = data.get('uploader')
#  self.uploader_url = data.get('uploader_url')
#  date = data.get('upload_date')
#  self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
#  self.title = data.get('title')
#  self.thumbnail = data.get('thumbnail')
#  self.description = data.get('description')
#  self.duration = self.parse_duration(int(data.get('duration')))
#self.tags = data.get('tags')
#self.url = data.get('webpage_url')
#self.views = data.get('view_count')
#self.likes = data.get('like_count')
#self.dislikes = data.get('dislike_count')
#self.stream_url = data.get('url')

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id=871748447055777883) # replace with channel_id
    while not client.is_closed():
        await channel.send(f"<@404613959568719872> is gay and likes kids!")
        await asyncio.sleep(1)


async def my_background_():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(id=796750832305307719) # replace with channel_id
    while not client.is_closed():
        counter += 1
        await channel.send(counter)
        await asyncio.sleep(1)

@commands.command(name="announce")
async def announce(ctx):
    # Find a channel from the guilds `text channels` (Rather then voice channels)
    # with the name announcements
    channel = discord.utils.get(ctx.guild.text_channels, name="announcements")
    if channel: # If a channel exists with the name

                embed = discord.Embed(color=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
                embed.set_author(name="Announcement", icon_url=ctx.client.user.avatar_url)
                embed.add_field(name=f"Sent by {ctx.message.author}", value=str("message"), inline=False)
                embed.set_thumbnail(url=ctx.client.user.avatar_url)
                embed.set_footer(text=ctx.client.user.name, icon_url=ctx.client.user.avatar_url)
                await ctx.message.add_reaction(emoji="✅")
                await channel.send(embed=embed)

#async def my_background():
#    await client.wait_until_ready()
#    channel = client.get_channel(id=796750832305307719) # replace with channel_id
#    while not client.is_closed():
#        await channel.send(f"<@559655984134488064> get to bed now!")
#        await channel.send(f"<@559655984134488064> get to bed now!")
#        await channel.send(f"<@559655984134488064> get to bed now!")
#        await channel.send(f"<@559655984134488064> get to bed now!")
#        await channel.send(f"<@559655984134488064> get to bed now!")
#        await channel.send(f"<@559655984134488064> get to bed now!")
#        await asyncio.sleep(1)


@slash.slash(description="Resume Audio")
@commands.has_role("Green Cap🟢")
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')

######this is for spamming for every 1 seconds 


@slash.slash(description="Pause Audio")
@commands.has_role("Green Cap🟢")
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')

@slash.slash(description="Stop The Audio")
@commands.has_role("Green Cap🟢")
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')

  


loop = asyncio.get_event_loop()
#client.loop.create_task(my_background_task())
#client.loop.create_task(my_background_())
#client.loop.create_task(my_background())
TOKEN = os.environ['TOKEN']
keep_alive()
client.run(TOKEN)