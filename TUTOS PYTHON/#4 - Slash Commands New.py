import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.event
async def on_ready():
    print("Bot opérationnel, Slash Commandes")
    try:
        synced = await bot.tree.sync()
        print(f"Nombres de commandes : {len(synced)}")
    except Exception as e:
        print(e)
    
@bot.hybrid_command(name="commands", description="Description de la commande.")
async def commande(ctx):
    await ctx.send(f'Par exemple de slashs commandes') 
    
bot.run('TOKEN ICI !')