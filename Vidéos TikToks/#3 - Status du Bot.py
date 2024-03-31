import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot Ok !')
    
@bot.command()
async def status(ctx, status: str):
    if status.lower() == 'online': 
        await bot.change_presence(status=discord.Status.online)
        await ctx.send("Status mis à jour : En Ligne.")
    elif status.lower() == 'dnd':
        await bot.change_presence(status=discord.Status.dnd)
        await ctx.send("Statut mis à jour : Ne pas déranger")
    elif status.lower() == 'idle':
        await bot.change_presence(status=discord.Status.idle)
        await ctx.send("Statut mis à jour : Inactif")
    elif status.lower() == 'stream':
        await bot.change_presence(activity=discord.Streaming(name='Test', url='Lien du stream twitch !'))
        await ctx.send("Statut mis à jour : En stream")
    else:
        await ctx.send("**Status Incorrect, veuillez précisez entre 'dnd', 'idle', 'stream', 'online'**")
        
        # Liste :
        # ONLINE : En Ligne
        # Dnd = Ne pas déranger
        # Idle = Inactif
        # Stream : Mise en stream (mettre un lien de stream valide dans url='' en direct.) 
        
bot.run('TOKEN ICI !')
    