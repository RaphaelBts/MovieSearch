import discord
from matcher.intents import botResponse


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

    response = botResponse(message.content)
    print(f'<{response}> has been send to Discord!')
    await message.channel.send(response)


client.run(TOKEN)