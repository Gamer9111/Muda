import discord, random
from discord.ext import commands
client=commands.Bot(command_prefix='?')
@client.command()
async def ?fart(ctx):
    await ctx.send('fart')
@client.command()
async def ?dm(ctx):
    await ctx.author.send('yup')
@client.command()
async def test(ctx):
    replies=['bruh test ok uh commas necessary?','bruh','test','ok','uh','nah','epic','poggers',]
    await ctx.send(random.choice(replies))
@client.command()
async def ?embed(ctx):
    embed=discord.Embed()
    embed.title='test'
    replies=['bruh','test','test2',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)
client.run('JTjYdQxbaou1thtK6Pk9E0mg4lXD3kNB')
