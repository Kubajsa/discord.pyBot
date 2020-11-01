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
    embed.add_field(name="About", value="Coded by Kubajsa in Python with <3. The GitHub repo for the bot is https://github.com/Kubajsa/discord.pyBot", inline= False)
    embed.add_field(name="Current commands", value=".commands .about .hello .ping .whois .trade [kit you want] [kit you have]", inline=False)
    embed.add_field(name="Current events", value="Automatically adds yes and no reactions in polls and suggestions. Deletes messages without images in 6b6t-screentshots. Events so far work only in http://discord.gg/m33xSJX", inline=False)
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
    embed.add_field(name=".whois @Kubajsa", value="Shows you some info about the user you mention", inline=False)
    embed.add_field(name=".trade kit_you_want kit_you_have", value="Makes a trade message", inline=False)
    embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command(aliases=['user'])
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title= member.display_name, description= member.mention, color= discord.Color.blue())
    embed.add_field(name="ID", value= member.id, inline= True)
    embed.add_field(name="Highest role", value= member.top_role.mention, inline= True)
    embed.add_field(name="Number of roles", value= str(len(member.roles)), inline= True)
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
    embed.add_field(name="Trade:", value=f"{ctx.author.mention} wants {kitwant} for {kithave}")
    await ctx.send(embed=embed)


client.run(os.environ['token'])
