from search import firstLinkSerch

import discord
from discord.ext import commands
from config import settings

filename = 'test2.wav' # your audio file name in WAV format

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() 
async def s(ctx): 
    author = ctx.message.author 

    await ctx.send(f'вот хуета: {firstLinkSerch(filename)}')

bot.run(settings['token'])
