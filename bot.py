import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_message(message):
    if str(message.channel.id) == "765885590918266920" or str(message.channel.id) == "765885184238288897":
        yes = discord.utils.get(message.guild.emojis, name='yes')
        no = discord.utils.get(message.guild.emojis, name='no')
        await message.add_reaction(yes)
        await message.add_reaction(no)
        print("Added a poll reaction")
    await client.process_commands(message)


@client.command()
async def hello(ctx):
    await ctx.channel.send("Hello " + str(ctx.author) + "!")


client.run(os.environ['token'])
