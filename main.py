import discord
from discord.ext import commands
import os


ARROW_LEFT = "⬅"
ARROW_RIGHT = "➡"

TOKEN = os.environ['key'] # Our token for discord bot to run


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', 
                   intents=intents)

#Bot.eve
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  # First menu here
  
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  print(f'Message from {message.author}: {message.content}')

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  await bot.process_commands(message)
  

@bot.command()
async def greetings(ctx, arg):

  await ctx.send(f'Hi {arg}')


@bot.command()
async def farewell(ctx, arg):

  await ctx.send(f'Bye {arg}')

@bot.command()
async def menu(ctx):
  custom = discord.Embed(
    title='Menu',
    description="This country is not supported, you can ask me to add it" 
    + "[here](https://degree-navigator.as.it.ubc.ca/dn4v/Login/dagdisclaimer.asp).",
    color=discord.Colour.blue()
  )
  custom.set_thumbnail(
  url='https://brand.ubc.ca/files/2018/09/Logos_1_2CrestDownload_768px.jpg')
  
  custom.add_field(
    name='!menu',
    value='List of all commands',
    inline=False
  )
  
  custom.add_field(
    name='!greetings',
    value='Says Hi',
    inline=False
  )
  
  custom.add_field(
    name='!farewell',
    value='Says Bye',
    inline=False
  )
  msg = await ctx.channel.send(embed=custom)

  await msg.add_reaction(ARROW_LEFT)
  await msg.add_reaction(ARROW_RIGHT)

  
@bot.event
async def on_reaction_add(reaction, user):
  print('Added reaction')
  await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


try:
  bot.run(TOKEN)
except:
  os.system("kill 1")
