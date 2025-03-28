import discord
from discord.ext import commands
import aiohttp
import asyncio

TOKEN = "TOKEN"  # Replace with your bot token securely
SOURCE_CHANNEL_ID = 123456789 # Your source channel ID here
TARGET_CHANNEL_ID = 123456789 # Your target channel ID here
WEBHOOK_URL = "" # Your webhook URL here

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

user_ids = set()

async def send_welcome_message(user_ids):
    mentions = " ".join([f"<@{user_id}>" for user_id in user_ids])
    welcome_message = f"""**Hej, {mentions} miło Was widzieć!**

Zechcecie opowiedzieć coś o sobie?

Nie musicie się do nich ograniczać, ale może poniższe pytania mogą w tym pomóc 🙂

1. Kim jesteś?
2. Co Cię pasjonuje?
3. Czym się zajmujesz?
4. Kto/co Cię do nas sprowadza?
5. Jakie jest Twoje ulubione jedzenie?

---

**Hey, nice to see you here! Would you like to introduce yourself?**

Those questions may help, but there's no need to limit yourself to them 🙂

1. Who are you?
2. What is your passion?
3. What do you do?
4. What/who brings you here?
5. What is your favourite food?"""

    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
        await webhook.send(content=welcome_message)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.channel.id == SOURCE_CHANNEL_ID:
        user_ids.add(message.author.id)
        
        if len(user_ids) == 3:  # When we have 3 users
            await send_welcome_message(user_ids)
            user_ids.clear()

    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx):
    global user_ids
    user_ids.clear()
    await ctx.send("User ID counter has been reset.")

bot.run(TOKEN)
