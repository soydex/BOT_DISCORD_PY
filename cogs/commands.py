import discord, aiohttp, os
from discord.ext import commands, tasks
from datetime import datetime

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bonjour(self, ctx):
        await ctx.send('Salut !',)

    @commands.command()
    async def stats(self, ctx, message_id: int):
        "Donne les statistiques d'un message présent sur le serveur."
        try:
            message = await ctx.channel.fetch_message(message_id)
            word_count = len(message.content.split())
            char_count = len(message.content)
            reaction_count = sum([reaction.count for reaction in message.reactions])
            reactions = {reaction.emoji: reaction.count for reaction in message.reactions}
            await ctx.send(f"Statistiques du message (ID: {message_id}):\n"
                           f"Nombre de mots: {word_count}\n"
                           f"Nombre de caractères: {char_count}\n"
                           f"Nombre total de réactions: {reaction_count}\n"
                           f"Réactions par emoji: {reactions}")
        except discord.NotFound:
            await ctx.send("Message introuvable.")

    @commands.command()
    async def aide(self, ctx):
        embed = discord.Embed(title="Commandes disponibles", color=discord.Color.blue())
        for command in self.client.commands:
            if not command.hidden:
                embed.add_field(name=f'.{command.name}', value=command.help or "Aucune description", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def reglement(self, ctx):
        "Réglement du serveur"
        example_embed = discord.Embed(
            title="Règlement du Serveur",
            type="rich",
            color=0xffffff,
            timestamp=datetime.now()  # Utilisation de datetime.now() pour obtenir l'horodatage actuel
        )   
        example_embed.add_field(name="", value="1. Restez positif et surtout soyez vigilant, nous sommes sur internet.", inline=False)
        example_embed.add_field(name="", value="2. Pas de spam ni d'autopromotion (invitations de serveurs, publicités, etc.) sans l'autorisation d'un modérateur du serveur, y compris via les MP envoyés aux autres membres.", inline=False)
        example_embed.add_field(name="", value="3. Pas de contenu obscène ou soumis à une limite d'âge, qu'il s'agisse de texte, d'images ou de liens mettant en scène de la nudité, du sexe, de l'hyperviolence ou tout autre contenu explicite perturbant.",inline=False)
        example_embed.add_field(name="", value="4. Éviter les sujets/contenus sensibles ou à tendance polémiques ainsi que la violence verbale. Que ce soit tout ce qui est en lien avec la violence ou qui puisse heurter la sensibilités d’autrui. Nous interdisons tous sujets qui peuvent être jugés polémique en fonction d’un contexte politique.",inline=False)

        await ctx.send(embed=example_embed)

    @commands.command()
    async def status(self, ctx, member : discord.Member=None):
        if member is None:
            member = ctx.author
        embed=discord.Embed(title=f"{member.name} your current status is", description= f'{member.activities[0].name}', color=0xcd32a7)
        await ctx.send(embed=embed)   

async def setup(client):
    await client.add_cog(Commands(client))
