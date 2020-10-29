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
    embed.add_field(name="Author", value="Coded by Kubajsa in Python with <3", inline= True)
    embed.add_field(name="Current commands", value=".about .hello .ping .whois .trade [kit you want] [kit you have]", inline=True)
    embed.add_field(name="Current events", value="Automatically adds yes and no reactions in polls and suggestions. Deletes messages without images in 6b6t-screentshots", inline=False)
    embed.set_thumbnail(url= client.user.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command(aliases=['user'])
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title= member.display_name, description= member.mention, color= discord.Color.blue())
    embed.add_field(name="ID", value= member.id, inline= True)
    embed.add_field(name="Highest role", value= member.top_role.mention, inline= True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def hello(ctx):
    await ctx.channel.send("Hello " + str(ctx.author) + "!")


@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def trade(ctx, kitwant, kithave):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="New trade!", description=f"Trade by: {ctx.author.mention}", color=discord.Color.orange())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="Trade:", value=f"{ctx.author.mention} wants {kithave} for {kitwant}")
    await ctx.send(embed=embed)


client.run(os.environ['token'])
