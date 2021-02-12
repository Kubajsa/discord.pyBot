import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(".about"))
    print("Bot is ready")


@client.event
async def on_message(message):
    if str(message.channel.id) == "765885590918266920" or str(message.channel.id) == "765885184238288897":
        yes = discord.utils.get(message.guild.emojis, name='yes')
        no = discord.utils.get(message.guild.emojis, name='no')
        await message.add_reaction(yes)
        await message.add_reaction(no)
        msgtext = message.content
        print("Added a poll reaction to message: " + msgtext)
    elif str(message.channel.id) == "771091645949149253" and not message.attachments:
        await message.channel.purge(limit=1)
    await client.process_commands(message)


@client.command()
async def about(ctx):
    embed = discord.Embed(title="Kubajsa's Bot", description="Here is some info about this bot:", color=discord.Color.dark_green())
    embed.add_field(name="About", value="Coded by @Kubajsa#0843 in Python with <3. The GitHub repo for the bot is https://github.com/Kubajsa/discord.pyBot", inline= False)
    embed.add_field(name="Current commands", value="Use .commands to view all available commands", inline=False)
    embed.set_thumbnail(url= client.user.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands", description="Commands and usages:", color=discord.Color.blue())
    embed.add_field(name=".about", value="Shows you some info about the bot", inline=False)
    embed.add_field(name=".commands", value="Shows this message", inline=False)
    embed.add_field(name=".hello", value="Says hello to you", inline=False)
    embed.add_field(name=".ping", value="Checks the bot's ping", inline=False)
    embed.add_field(name=".whois @Kubajsa", value="Alias: .user\nShows you some info about the user you mention", inline=False)
    embed.add_field(name=".avatar @Kubajsa", value="Shows you the avatar of the person you mention", inline=False)
    embed.add_field(name=".server", value="Shows you info about the server", inline=False)
    embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command(aliases=['user'])
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title= member.display_name, description= member.mention, color= discord.Color.blue())
    embed.add_field(name="ID", value= member.id, inline= True)
    embed.add_field(name="Highest role", value= member.top_role.mention, inline= True)
    embed.add_field(name="Number of roles", value= str(len(member.roles) - 1), inline= True)
    embed.add_field(name="Joined at", value= member.joined_at.strftime("%d %B, %Y"), inline= False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def avatar(ctx, member : discord.Member):
    embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.blue())
    embed.set_image(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def server(ctx):
    embed = discord.Embed(title="Server Information", color=discord.Color.blue())
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="🌇Server name:", value=ctx.guild.name, inline=False)
    embed.add_field(name="🗺️Region:", value=str(ctx.guild.region).capitalize(), inline=False)
    embed.add_field(name="😂Emojis:", value=str(len(ctx.guild.emojis)), inline=False)
    embed.add_field(name="💯Role Count:", value=str(len(ctx.guild.roles)), inline=False)
    embed.add_field(name="🧑‍🤝‍🧑Members:", value=str(ctx.guild.member_count), inline=False)
    embed.add_field(name="💬Channels:", value=str(len(ctx.guild.channels)), inline=False)
    embed.add_field(name="🔊Voice Channels:", value=str(len(ctx.guild.voice_channels)), inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def hello(ctx):
    await ctx.channel.send("Hello " + str(ctx.author) + "!")


@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')


client.run(os.environ['token'])
