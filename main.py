import discord
from discord import app_commands
from discord.ext import commands
from youtubesearchpython import VideosSearch
from discord import FFmpegPCMAudio
from discord.utils import get
import youtube_dl
import yt_dlp
import asyncio
import requests
# from discord_components import create_select_option

client = commands.Bot(command_prefix="!",intents = discord.Intents.all())

@client.event
async def on_ready():
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
    try:
        sycned = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name="hello",description="this command says hello back")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey")

@client.tree.command(name="help",description="This Is A List of Commands For The Music:")
# @app_commands.describe(description="This Is A List of Commands For The Music:")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="MUSIC BOT (YOUTUBE)",description="List of commands:",color=discord.Color.blue())
    embed.add_field(name="/play (Youtube/Soundcloud-Link)",value="This play the youtube/soundcloud audio through the discord bot.",inline=False)
    embed.add_field(name="/search (key word/phrase)",value="This will search youtube and find all the videos relating to that search and give you a list of options to choose from",inline=False)
    embed.add_field(name="/pause",value="This pause the music audio.",inline=False)
    embed.add_field(name="/resume",value="This will resume the audio.",inline=False)
    embed.set_thumbnail(url=interaction.guild.icon.url)
    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.avatar.url)
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="play", description="Make The Bot Play Any Youtube Video.")
async def play(interaction: discord.Interaction, url: str):
    voice_client = get(client.voice_clients, guild=interaction.guild)
    if not voice_client:
        if not interaction.user.voice:
            await interaction.response.send_message("You are not connected to a voice channel.",ephemeral=True)
            return
        voice_channel = interaction.user.voice.channel
        voice_client = await voice_channel.connect()
    elif voice_client.is_playing():
        voice_client.stop()
    with yt_dlp.YoutubeDL({'format': 'bestaudio'}) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['url']
        title = info['title']
        uploader = info['uploader']
        thumbnail = info['thumbnail']
    embed = discord.Embed(title="Song", description="Details:", color=discord.Color.blue())
    embed.add_field(name="Song Name:", value=title, inline=False)
    embed.add_field(name="Song/Audio By:", value=uploader, inline=False)
    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.avatar.url)
    embed.set_thumbnail(url=thumbnail)
    voice_client.play(discord.FFmpegPCMAudio(URL))
    print(f"{interaction.user} has just played:")
    print(f"Title: {title} - Uploader: {uploader} - Link: {url}")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="search", description="Make The Bot Play Any Youtube Video but uses words instead of a URL")
async def search(interaction: discord.Interaction, search: str):
    videosSearch = VideosSearch(search, limit=5)
    videos = videosSearch.result()
    options = [
        discord.SelectOption(label=videos["result"][0]["title"], description=videos["result"][0]["channel"]["name"]),
        discord.SelectOption(label=videos["result"][1]["title"], description=videos["result"][1]["channel"]["name"]),
        discord.SelectOption(label=videos["result"][2]["title"], description=videos["result"][2]["channel"]["name"]),
        discord.SelectOption(label=videos["result"][3]["title"], description=videos["result"][3]["channel"]["name"]),
        discord.SelectOption(label=videos["result"][4]["title"], description=videos["result"][4]["channel"]["name"]),
    ]   

    class YoutuberDropdown(discord.ui.Select):
        def __init__(self):
            super().__init__(placeholder="Select a video to play", options=options, min_values=1, max_values=1)

        async def callback(self, interaction: discord.Interaction):
            selected_option = self.values[0]
            for video in videos["result"]:
                if video["title"] == selected_option:
                    url = video["link"]
                    voice_client = get(client.voice_clients, guild=interaction.guild)
                    if not voice_client:
                        if not interaction.user.voice:
                            await interaction.response.send_message("You are not connected to a voice channel.",ephemeral=True)
                            return
                        voice_channel = interaction.user.voice.channel
                        voice_client = await voice_channel.connect()
                    elif voice_client.is_playing():
                        voice_client.stop()
                    with yt_dlp.YoutubeDL({'format': 'bestaudio'}) as ydl:
                        info = ydl.extract_info(url, download=False)
                        URL = info['url']
                        title = info['title']
                        uploader = info['uploader']
                        thumbnail = info['thumbnail']
                    embed = discord.Embed(title="Song", description="Details:", color=discord.Color.blue())
                    embed.add_field(name="Song Name:", value=title, inline=False)
                    embed.add_field(name="Song/Audio By:", value=uploader, inline=False)
                    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.avatar.url)
                    embed.set_thumbnail(url=thumbnail)
                    voice_client.play(discord.FFmpegPCMAudio(URL))
                    print(f"{interaction.user} has just played:")
                    print(f"Title: {title} - Uploader: {uploader} - Link: {video['link']}")
                    await interaction.response.send_message(embed=embed)
                    self.view.remove_item(self)
                    break

    class YoutuberView(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(YoutuberDropdown())

    await interaction.response.send_message("Click the dropdown below", view=YoutuberView(), ephemeral=True)

@client.tree.command(name="pause",description="Pause the current song.")
async def pause(interaction: discord.Interaction):
    voice_client = get(client.voice_clients, guild=interaction.guild)
    if voice_client.is_playing():
        voice_client.pause()
        await interaction.response.send_message("Song has been paused.")
    else:
        await interaction.response.send_message("The bot is not currently playing any song.")

@client.tree.command(name="resume",description="Resume the current song.")
async def resume(interaction: discord.Interaction):
    voice_client = get(client.voice_clients, guild=interaction.guild)
    if voice_client.is_paused():
        voice_client.resume()
        await interaction.response.send_message("Song has been resumed.")
    else:
        await interaction.response.send_message("The bot is not currently paused.")

async def clear(interaction: discord.Interaction):
    await interaction.response.send_message("The bot is not currently paused.")

client.run("TOKEN-HERE")
