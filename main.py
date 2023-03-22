from datetime import datetime
import discord
import os
from discord.ext import commands
import random
# from webserver import keep_alive
from discord import FFmpegPCMAudio
from discord.utils import get
from youtube_dl import YoutubeDL
import asyncio
from youtubesearchpython import VideosSearch
#from discord_buttons_plugin import *
from discord_slash import SlashCommand
#pip install -U discord-py-slash-command
import keep_alive

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(commands.when_mentioned_or("."),
                      case_insensitive=True,
                      intents=intents)
#buttons = ButtonsClient(client)
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    #while True:
    #  print("txt was cleared")
    #  await asyncio.sleep(20)
    #  with open("spam_detect.txt","r+") as file:
    #    file.truncate(0)
    await client.change_presence(activity=discord.Game(name="MUSIC |  /help"))
    print(r"""\

                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /

                Music Bot is online!
            """)


@client.event
async def on_message(message):
    if str(message.channel) == "r-u-l-e-s" and message.content != "":
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


@slash.slash(description="This Is A List of Commands For The Music:")
async def help(ctx):
    embed = discord.Embed(title="MUSIC BOT (YOUTUBE)",
                          description="List of commands:",
                          color=discord.Color.blue())
    embed.add_field(name="/join",
                    value="This will make the bot join your vc you are in.",
                    inline=False)
    embed.add_field(name="/play (Youtube-Link)",
                    value="This play the youtube audio.",
                    inline=False)
    embed.add_field(name="/pause",
                    value="This pause the music audio.",
                    inline=False)
    embed.add_field(name="/resume",
                    value="This will resume the audio.",
                    inline=False)
    embed.add_field(name="/stop",
                    value="This will restart the music if any issues.",
                    inline=False)
    embed.add_field(name="/leave or .disconnect",
                    value="This will kick the bot from the vc the bot is in.",
                    inline=False)
    await ctx.send(embed=embed)


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
async def leave(context):
    channel = context.author.voice.channel
    await context.voice_client.disconnect()
    await context.send(f"The bot has left {channel}")


@slash.slash(description="Make The Bot Leave Your Vc.")
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

@slash.slash(name='join',
             description='Tells the bot to join the voice channel')
async def join(Context):
    channel = Context.author.voice.channel
    await channel.connect()
    await Context.send(f"The Bot Has Joined {channel}")

@slash.slash(description="Play any audio from link.")
async def link(Context, url):
    YDL_OPTIONS = {
        'format': 'bestaudio/best',
        'noplaylist': 'True',
        'default_search': 'auto',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'audioformat': 'mp3',
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
    }
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    voice = get(client.voice_clients, guild=Context.guild)
    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            info_dict = ydl.extract_info(url, download=False)
        URL = info['url']
        title = info['title']
        uploader = info['uploader']
        thumbnail = info['thumbnail']
        print(thumbnail)
        embed = discord.Embed(title="Song",
                              description="Details:",
                              color=discord.Color.blue())
        embed.add_field(name="Song Name:", value=title, inline=False)
        embed.add_field(name="Song/Audio By:", value=uploader, inline=False)
        embed.set_footer(text=f"Requested by {Context.author}",
                         icon_url=Context.author.avatar_url)
        embed.set_thumbnail(url=thumbnail)
        try:
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await Context.send(embed=embed)
            # await Context.send(f'Bot is now playing: **{title}** 🎵  \nBy: **{uploader}**')
            print(f"The video: {title} is now downloaded")
        except:
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await Context.send(embed=embed)
            # await Context.send(f'Bot is now playing: **{title}** 🎵  \nBy: **{uploader}**')
            print(f"The video: {title} is now downloaded")

    else:
        await Context.send(f"Bot is already playing: **{title}**")
        return


@slash.slash(description="Make The Bot Play Any Youtube Video.")
async def play(Context, search):
    videosSearch = VideosSearch(search, limit=1)
    url = videosSearch.result()["result"][0]["link"]
    YDL_OPTIONS = {
        'format': 'bestaudio/best',
        'noplaylist': 'True',
        'default_search': 'auto',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'audioformat': 'mp3',
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
    }
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    voice = get(client.voice_clients, guild=Context.guild)
    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            info_dict = ydl.extract_info(url, download=False)
        URL = info['url']
        title = info['title']
        uploader = info['uploader']
        thumbnail = info['thumbnail']
        print(thumbnail)
        embed = discord.Embed(title="Song",
                              description="Details:",
                              color=discord.Color.blue())
        embed.add_field(name="Song Name:", value=title, inline=False)
        embed.add_field(name="Song/Audio By:", value=uploader, inline=False)
        embed.set_footer(text=f"Requested by {Context.author}",
                         icon_url=Context.author.avatar_url)
        embed.set_thumbnail(url=thumbnail)
        try:
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await Context.send(embed=embed)
            # await Context.send(f'Bot is now playing: **{title}** 🎵  \nBy: **{uploader}**')
            print(f"The video: {title} is now downloaded")
        except:
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await Context.send(embed=embed)
            # await Context.send(f'Bot is now playing: **{title}** 🎵  \nBy: **{uploader}**')
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
    channel = client.get_channel(
        id=871748447055777883)  # replace with channel_id
    while not client.is_closed():
        await channel.send(f"<@404613959568719872> is gay and likes kids!")
        await asyncio.sleep(1)


async def my_background_():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(
        id=796750832305307719)  # replace with channel_id
    while not client.is_closed():
        counter += 1
        await channel.send(counter)
        await asyncio.sleep(1)


@commands.command(name="announce")
async def announce(ctx):
    # Find a channel from the guilds `text channels` (Rather then voice channels)
    # with the name announcements
    channel = discord.utils.get(ctx.guild.text_channels, name="announcements")
    if channel:  # If a channel exists with the name

        embed = discord.Embed(color=discord.Color.dark_gold(),
                              timestamp=ctx.message.created_at)
        embed.set_author(name="Announcement",
                         icon_url=ctx.client.user.avatar_url)
        embed.add_field(name=f"Sent by {ctx.message.author}",
                        value=str("message"),
                        inline=False)
        embed.set_thumbnail(url=ctx.client.user.avatar_url)
        embed.set_footer(text=ctx.client.user.name,
                         icon_url=ctx.client.user.avatar_url)
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
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')


######this is for spamming for every 1 seconds


@slash.slash(description="Pause Audio")
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')


@slash.slash(description=f"Harsh being naughty")
async def harsh(Context):
    channel = Context.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("harsh.mp3")
    player = voice.play(source)
    await asyncio.sleep(6)
    await Context.voice_client.disconnect()


@slash.slash(description=f"Poki Poki")
async def poki(Context):
    channel = Context.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("poki.mp3")
    player = voice.play(source)
    await asyncio.sleep(15)
    await Context.voice_client.disconnect()


@slash.slash(description="Stop The Audio")
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
# keep_alive.keep_alive()
client.run(TOKEN)
