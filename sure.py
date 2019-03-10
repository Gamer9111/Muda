import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = '/')
Clientdiscord = discord.Client()
@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Wow you joined this cancer, why? Prefix is /')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name="No"))

@client.event
async def on_message(message):
    if message.content.startswith('Bowsette'):
        await client.send_message(message.channel,'(0.author.mention) No')
    if message.content.startswith('/Gay?'):
        randomlist = ["yes","no","big yes","suprisingly no"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('/Coinflip'):
        randomlist = ["Heads","Tails"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('/Dice'):
        randomlist = ["1","2","3","4","5","6"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '/DIO':
        em = discord.Embed(description='(0.author.mention) ZA WARUDO')
        em.set_image(url='https://cdn.discordapp.com/attachments/490251540905328642/491716618897063936/tenor.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '/Help':
        await client.send_message(message.channel,'commands are /Help /DIO /Gay? /Dice /Coinflip /Whogay?')
    if message.content.startswith('/Whogay?'):
        randomlist = ["U","Fag Above You","The Fag Above The Fag Above You","The Next Prick Who Types","The Prick after the Next Prick Who Types"]
    if message.content == 'MUDA MUDA MUDA':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/491716472779833346/493922656278806528/MUDA_ORA_MUDA_ORA_MUDA_ORA.gif')
    if message.content == 'ORA ORA ORA':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/491716472779833346/493922656278806528/MUDA_ORA_MUDA_ORA_MUDA_ORA.gif')
    if message.content == 'ur mum gay':
        msg = 'No U Cunt https://cdn.discordapp.com/attachments/491716472779833346/493927255479812096/2Q.png'.format(message)
    if message.content == '/Invite':
        await client.send_message(message.channel,'https://discordapp.com/oauth2/authorize?client_id=491724307378995219&scope=bot&permissions=8')

client.run(os.getenv('TOKEN'))
