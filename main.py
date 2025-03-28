import discord
from discord.ext import commands

TOKEN = "TOKEN"  # Replace with your bot token securely
SOURCE_CHANNEL_ID = 1172246680662454314
TARGET_CHANNEL_ID = 1193592031008788632

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
# intents.message_content = True  # Disabled to avoid privileged intents error

bot = commands.Bot(command_prefix="!", intents=intents)

user_ids = set()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.channel.id == SOURCE_CHANNEL_ID:
        user_ids.add(message.author.id)
        
        if len(user_ids) == 1:
            target_channel = bot.get_channel(TARGET_CHANNEL_ID)
            if target_channel:
                ids_str = ", ".join(map(str, user_ids))
                await target_channel.send(f"Three user IDs: {ids_str}")
            user_ids.clear()

    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx):
    global user_ids
    user_ids.clear()
    await ctx.send("User ID counter has been reset.")

bot.run(TOKEN)
