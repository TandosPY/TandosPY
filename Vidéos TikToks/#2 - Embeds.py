import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.event
async def on_ready():
    print(f'Bot ON !')
    
   
@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="Test", description="Test Test test", color=discord.Color.green())
    
    embed.set_footer(text="Footer Pour une vidéo.")
    await ctx.send(embed=embed)
   
bot.run('TOKEN ICI !')