import discord
from discord.ext import commands
import datetime

LOG_CHANNEL_NAME = 'logs'
VOICE_CHANNEL_ID = 1250807430552490054

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.id == self.bot.user.id:
            return
        
        log_channel = discord.utils.get(message.guild.text_channels, name=LOG_CHANNEL_NAME)
        if log_channel:
            embed = discord.Embed(title="Message supprimé", color=discord.Color.red())  # Initialize the embed first
            if message.author.avatar:
                embed.set_thumbnail(url=message.author.avatar.url)
            
            embed.add_field(name="Auteur", value=message.author.mention, inline=True)
            embed.add_field(name="Contenu", value=message.content, inline=False)
            embed.set_footer(text=f"ID de l'utilisateur: {message.author.id} • ID du message: {message.id}")
            embed.timestamp = datetime.datetime.utcnow()
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        log_channel = discord.utils.get(before.guild.text_channels, name=LOG_CHANNEL_NAME)
        if before.author.id == self.bot.user.id:
            return  
        elif after.author.id == self.bot.user.id:
            return
        if log_channel:
            embed = discord.Embed(title="Message édité", color=discord.Color.orange())
            if isinstance(after.author, discord.Member) and after.author.avatar:
                embed.set_thumbnail(url=after.author.avatar.url)
            embed.add_field(name="Auteur", value=before.author.mention, inline=True)
            embed.add_field(name="Avant", value=before.content, inline=False)
            embed.add_field(name="Après", value=after.content, inline=False)
            embed.set_footer(text=f"ID de l'utilisateur: {before.author.id} • ID du message: {before.id}")
            embed.timestamp = datetime.datetime.utcnow()
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = discord.utils.get(member.guild.text_channels, name=LOG_CHANNEL_NAME)
        if log_channel:
            embed.set_thumbnail(url=member.avatar.url)
            embed = discord.Embed(title="Nouveau membre", description=f"{member.mention} a rejoint la Brigade AMG.", color=discord.Color.green())
            embed.set_footer(text=f"ID de l'utilisateur: {member.id}")
            await log_channel.send(embed=embed)



    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = discord.utils.get(member.guild.text_channels, name=LOG_CHANNEL_NAME)
        if log_channel:
            embed = discord.Embed(title="Membre parti", description=f"{member.mention} a quitté le serveur.", color=discord.Color.red())
            
            avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
            embed.set_thumbnail(url=avatar_url)

            embed.set_footer(text=f"ID de l'utilisateur: {member.id}")
            embed.timestamp = datetime.datetime.utcnow()
            await log_channel.send(embed=embed)
        guild = member.guild
        voice_channel = discord.utils.get(guild.channels, id=VOICE_CHANNEL_ID)
        if voice_channel:
            await voice_channel.edit(name=f'Membres : {guild.member_count}')


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        log_channel = discord.utils.get(member.guild.text_channels, name=LOG_CHANNEL_NAME)
        if log_channel:
            if before.channel is None and after.channel is not None:
                embed = discord.Embed(title="Connexion vocale", description=f"{member} a rejoint le salon vocal {after.channel.name}", color=discord.Color.blue())
            elif before.channel is not None and after.channel is None:
                embed = discord.Embed(title="Déconnexion vocale", description=f"{member} a quitté le salon vocal {before.channel.name}", color=discord.Color.blue())
            elif before.channel != after.channel:
                embed = discord.Embed(title="Changement de salon vocal", description=f"{member} a changé de salon vocal {before.channel.name} -> {after.channel.name}", color=discord.Color.blue())
            embed.set_thumbnail(url=member.avatar.url)
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        log_channel = discord.utils.get(before.guild.text_channels, name=LOG_CHANNEL_NAME)
        if log_channel:
            embed = discord.Embed(title="Rôle modifié", description=f"Le rôle {before.name} a été modifié.", color=discord.Color.purple())
            if before.name != after.name:
                embed.add_field(name="Nom", value=f"{before.name} -> {after.name}", inline=False)
            if before.permissions != after.permissions:
                embed.add_field(name="Permissions", value=f"{before.permissions} -> {after.permissions}", inline=False)
            if before.color != after.color:
                embed.add_field(name="Couleur", value=f"{before.color} -> {after.color}", inline=False)
            embed.set_thumbnail(url=before.author.avatar.url)
            embed.set_footer(text=before.author.name)
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        log_channel = discord.utils.get(before.guild.text_channels, name=LOG_CHANNEL_NAME)
        if log_channel:
            before_roles = set(before.roles)
            after_roles = set(after.roles)
            added_roles = after_roles - before_roles
            removed_roles = before_roles - after_roles

            embed = discord.Embed(title="Modification des rôles", description=f"Modifications des rôles pour {after.display_name}.", color=discord.Color.teal())
            if added_roles:
                embed.add_field(name="Rôles ajoutés", value=", ".join([role.name for role in added_roles]), inline=False)
            if removed_roles:
                embed.add_field(name="Rôles retirés", value=", ".join([role.name for role in removed_roles]), inline=False)
            embed.set_thumbnail(url=before.author.avatar.url)
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, commands.CheckFailure):
            await ctx.send(f"{ctx.author.mention}, vous n'avez pas la permission d'exécuter la commande `{ctx.command}`.")
            print(f"{ctx.author} does not have permission to run `{ctx.command}`")
        elif isinstance(exception, commands.CommandNotFound):
            await ctx.send(f"La commande `{ctx.invoked_with}` n'a pas été trouvée.")
            print(f"Command `{ctx.invoked_with}` not found")
        elif isinstance(exception, commands.MissingRequiredArgument):
            await ctx.send(f"Il manque un argument requis pour la commande `{ctx.command}`. Veuillez vérifier votre syntaxe et réessayer.")
            print(f"Missing required argument for command `{ctx.command}`")
        elif isinstance(exception, commands.BadArgument):
            await ctx.send(f"Un des arguments fournis pour la commande `{ctx.command}` est invalide. Veuillez vérifier votre syntaxe et réessayer.")
            print(f"Bad argument for command `{ctx.command}`")
        elif isinstance(exception, commands.CommandOnCooldown):
            await ctx.send(f"La commande `{ctx.command}` est en cooldown. Veuillez réessayer dans {exception.retry_after:.2f} secondes.")
            print(f"Command `{ctx.command}` is on cooldown. Retry after {exception.retry_after:.2f} seconds")
        elif isinstance(exception, commands.DisabledCommand):
            await ctx.send(f"La commande `{ctx.command}` est actuellement désactivée.")
            print(f"Command `{ctx.command}` is disabled")
        elif isinstance(exception, commands.NoPrivateMessage):
            await ctx.send(f"La commande `{ctx.command}` ne peut pas être utilisée en message privé.")
            print(f"Command `{ctx.command}` cannot be used in private messages")
        else:
            print(exception)



async def setup(bot):
    await bot.add_cog(test(bot))
