import discord
from discord.ext import commands
import tracemalloc
import datetime
import os
import secu

tracemalloc.start()

# Clear console
os.system('cls' if os.name == 'nt' else 'clear')

# Initialize bot
intents = discord.Intents.all()
client = commands.Bot(command_prefix=commands.when_mentioned_or('.'), intents=intents)

# List of cogs to load
cog_files = ['cogs.moderation', 'cogs.logs', 'cogs.commands']

@client.event
async def on_ready():
    for cog_file in cog_files:
        try:
            await client.load_extension(cog_file)
            print(f"{cog_file} has loaded.")
        except Exception as e:
            print(f"Failed to load {cog_file}: {e}")
    print(f"We have logged in as {client.user}")
    servers = {guild.id: guild.name for guild in client.guilds}
    print("Server IDs and Names:")
    for guild_id, guild_name in servers.items():
        print(f"Guild ID: {guild_id}, Guild Name: {guild_name}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".gg/antimg"))

@client.command()
async def reload(ctx, arg):
    try:
        await client.reload_extension(f"cogs.{arg}")
        await ctx.send("Extension reloaded successfully")
    except commands.ExtensionNotLoaded:
        await ctx.send("Extension was not loaded")
    except commands.ExtensionNotFound:
        await ctx.send("Extension not found")
    except commands.ExtensionFailed as e:
        await ctx.send(f"Extension failed to reload: {e}")

# Run the bot
if __name__ == "__main__":
    client.run(secu.TOKEN_soydex)