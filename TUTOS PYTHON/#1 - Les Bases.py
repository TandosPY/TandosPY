import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.event
async def on_ready():
    print(f'Bot ON !')
    
@bot.command() 
async def commande(ctx):
    await ctx.send(f'Texte Ici :)')
    
bot.run('TOKEN ICI !')