import discord, datetime
from discord.ext import commands

class ModerationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="kick")
    async def my_kick_command(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f"{member} has been kicked for {reason}.")
        else:
            await ctx.send("You do not have permission to kick members.")

    @commands.command(name="clear")
    async def clear(self, ctx, nombre: int):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=nombre + 1)
            await ctx.send(f"{nombre} messages ont été effacés.", delete_after=5)  
        else:
            await ctx.send("Vous n'avez pas la permission de gérer les messages.")

    @commands.command(name= "cree_role")
    async def creer_role(self,ctx, nom_role):
        guild = ctx.guild
        if discord.utils.get(guild.roles, name=nom_role) is None:
            await guild.create_role(name=nom_role)
            await ctx.send(f"Le rôle '{nom_role}' a été créé avec succès.")
        else:
            await ctx.send("Ce rôle existe déjà.")

    @commands.command(name= "ajouter_role")
    async def ajouter_role(self,ctx,nom_role, user: discord.Member):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name=nom_role)
        if role is not None:
            await user.add_roles(role)
            await ctx.send(f"Le rôle '{nom_role}' a été ajouté à {user.mention} avec succès.")
        else:
            await ctx.send("Ce rôle n'existe pas.")

    @commands.command()
    async def move_all(self, ctx):
        "téléporte tous les utilisateurs dans mon salon vocal"
        author_voice_channel = ctx.author.voice.channel
        if author_voice_channel is None:
            await ctx.send("Vous devez être connecté à un salon vocal pour utiliser cette commande.")
            return
        for member in ctx.guild.members:  # Itérer à travers les membres du serveur
            if member.voice is not None and member.voice.channel is not None:  # Vérifier si le membre est connecté à un salon vocal
                await member.move_to(author_voice_channel)
        await ctx.send(f"Tous les membres ont été déplacés vers {author_voice_channel.name}.")

    @commands.command()
    async def voc(self,ctx):
        voice_channel_members = 0
        for guild in self.client.guilds:
            for voice_channel in guild.voice_channels:
                voice_channel_members += len(voice_channel.members)
        embed = discord.Embed(title="Personnes en vocal", description=".gg/antimg")
        embed.set_author(name=self.client.user.display_name, url="https://discord.com/invite/antimg", icon_url=self.client.user.avatar.url if self.client.user.avatar else None)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
        embed.add_field(name="Vocaux", value=f"{voice_channel_members} personnes connectées", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)    


async def setup(bot):
    await bot.add_cog(ModerationCommands(bot))
