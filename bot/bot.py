import discord

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
    if message.author == client.user:
        return 
        
    if message.content == "Commands":
        await message.channel.send(" Differents users requets can be made /n")

@client.event
async def on_message(message):
    # avoid self response
    if message.author == client.user:
        return

    if message.content == 'test':
        await message.channel.send("reply to test")

client.run(TOKEN)