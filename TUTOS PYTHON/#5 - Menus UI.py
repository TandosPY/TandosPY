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

class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="NOM DE LA CATEGORIE", emoji="EMOJI", description="Description"),
        ]
        super().__init__(placeholder="Nom de l'interieur du menu", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        selected_option = self.values[0]
        if selected_option == "NOM DE LA CATEGORIE":
            embed = discord.Embed(
                title="titre de l'embed",
                description="description",
                color=discord.Color.blue()
            )

class SelectView(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(Select())
    
@bot.hybrid_command(name="Nom de ta commande", description="Description de ta commande")
async def Commande(ctx):
    member = ctx.author
    embed = discord.Embed(
        title=f"Titre de l'embed à envoyer avec le menu",
        description="**Description de l'embed*",
        color=discord.Color.blue()
    )
    

    await ctx.send(embed=embed, view=SelectView())
    
bot.run('TOKEN ICI !')