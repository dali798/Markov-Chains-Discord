import discord
import markov
import os
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        filenames = sys.argv[1:]
        text = markov.open_and_read_file(filenames)
        chains = markov.make_chains(text)
        string = markov.make_text(chains)
        await message.channel.send(string)

client.run(os.environ["DISCORD_TOKEN"])
