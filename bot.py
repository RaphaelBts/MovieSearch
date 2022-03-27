import discord
from matcher.intents import botResponse

import time


TOKEN = "OTQ3NDYyNjQxOTMxMTQ1MjQ3.YhtnWA.tn7agP_In8cM3O7GFOoC8TmEqdI"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
    

@client.event
async def on_message(message):
    # avoid self response
    if message.author == client.user:
        return

    content = botResponse(message.content)
    response = content[1]
    embed2 = discord.Embed(title= content[0], description=response, color=discord.Color.blue())

    response = response[:5000]
    chunks = getChunks(response)
    for chunk in chunks:
        print(len(chunk))
        print(chunk)
        embed3 = discord.Embed( description=chunk, color=discord.Color.blue())
        await message.channel.send(embed=embed3)
        time.sleep(2)
  
    #await message.channel.send(response)
    await message.channel.send(embed=embed2)
    print(f'\033[92m<{len(response)}> characters has been send to Discord!\033[0m')

def getChunks(text, chunksize=6000):
    chunks = []
    block = []
    line = []

    for ptr in range(len(text)):
        line += text[ptr]
        if text[ptr] == '\n':
            if len(block + line) < chunksize:
                block += line
                line = []
            else:
                chunks.append(''.join(block))
                block = line

        if ptr == len(text):
            chunks.append(''.join(block))

    return chunks

client.run(TOKEN)