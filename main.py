import discord
from discord.ext import commands
import aiohttp
import asyncio
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
SOURCE_CHANNEL_ID = int(os.getenv('SOURCE_CHANNEL_ID'))
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID'))
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

# Validate environment variables
if not all([TOKEN, SOURCE_CHANNEL_ID, TARGET_CHANNEL_ID, WEBHOOK_URL]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

QUESTIONS = [
    ("Jakie jest Twoje ulubione jedzenie?", "What is your favourite food?"),
    ("Jakie masz marzenia?", "What are your dreams?"),
    ("Jakie supermoce chciałbyś/chciałabyś posiadać?", "What superpowers would you like to have?"),
    ("Jaki jest Twój ulubiony film?", "What is your favourite movie?"),
    ("Gdzie chciałbyś/chciałabyś mieszkać?", "Where would you like to live?"),
    ("Jaki jest Twój ulubiony kolor?", "What is your favourite color?"),
    ("Co robisz w wolnym czasie?", "What do you do in your free time?"),
    ("Jaki jest Twój ulubiony sport?", "What is your favourite sport?"),
    ("Jaki jest Twój ulubiony gatunek muzyki?", "What is your favourite music genre?"),
    ("Jaka jest Twoja ulubiona pora roku?", "What is your favourite season?"),
    ("Jaka jest Twoja ulubiona książka?", "What is your favourite book?"),
    ("Jakie kraje chciałbyś/chciałabyś odwiedzić?", "Which countries would you like to visit?"),
    ("Jaka była Twoja najlepsza podróż?", "What was your best trip?"),
    ("Czy wierzysz w życie pozaziemskie?", "Do you believe in extraterrestrial life?"),
    ("Jaki jest Twój ulubiony zwierzak?", "What is your favourite animal?"),
    ("Gdybyś mógł/mogła cofnąć się w czasie, do jakiej epoki byś się udał/a?", "If you could travel back in time, which era would you visit?"),
    ("Gdybyś mógł/mogła zamienić się ciałem z kimś na jeden dzień, kto by to był?", "If you could switch bodies with someone for a day, who would it be?"),
    ("Jakie jest Twoje największe osiągnięcie?", "What is your greatest achievement?"),
    ("Jaki jest Twój ulubiony cytat?", "What is your favourite quote?"),
    ("Gdybyś mógł/mogła nauczyć się dowolnej umiejętności w jeden dzień, co by to było?", "If you could learn any skill in one day, what would it be?"),
    ("Jakie jest Twoje wymarzone miejsce na wakacje?", "What is your dream vacation destination?"),
    ("Czy wolisz morze czy góry?", "Do you prefer the sea or mountains?"),
    ("Jakie jest Twoje ulubione danie z dzieciństwa?", "What is your favourite childhood dish?"),
    ("Jaki jest Twój ulubiony sposób spędzania weekendu?", "What is your favourite way to spend the weekend?"),
    ("Gdybyś mógł/mogła zagrać w dowolnym filmie, jaki by to był?", "If you could act in any movie, which one would it be?"),
    ("Jakie jest Twoje ulubione święto?", "What is your favourite holiday?"),
    ("Czy wolisz filmy czy seriale?", "Do you prefer movies or TV series?"),
    ("Jakiej jednej rzeczy nigdy byś nie zrobił/a?", "What is one thing you would never do?"),
    ("Czy wolisz kawę czy herbatę?", "Do you prefer coffee or tea?"),
    ("Jaka jest Twoja ulubiona gra komputerowa lub planszowa?", "What is your favourite video or board game?"),
    ("Czy masz jakieś hobby?", "Do you have any hobbies?"),
    ("Jak wyglądałby Twój idealny dzień?", "What would your perfect day look like?"),
    ("Gdybyś miał/miała napisać książkę, o czym by była?", "If you were to write a book, what would it be about?"),
    ("Czy wolisz wczesne poranki czy późne noce?", "Do you prefer early mornings or late nights?"),
    ("Jakie jest Twoje ulubione zwierzę domowe?", "What is your favourite pet?"),
    ("Jaki był Twój najlepszy prezent, jaki kiedykolwiek dostałeś/aś?", "What was the best gift you ever received?"),
    ("Czy wolisz słuchać muzyki czy czytać książki?", "Do you prefer listening to music or reading books?"),
    ("Jaka jest Twoja ulubiona piosenka?", "What is your favourite song?"),
    ("Czy wolisz być sam/a czy wśród ludzi?", "Do you prefer being alone or with people?"),
    ("Jaki jest Twój ulubiony gatunek filmowy?", "What is your favourite movie genre?"),
    ("Czy masz jakieś fobie?", "Do you have any phobias?"),
    ("Gdybyś mógł/mogła spotkać dowolną osobę, żyjącą lub nie, kto by to był?", "If you could meet anyone, living or dead, who would it be?"),
    ("Jakie jest Twoje ulubione miasto?", "What is your favourite city?"),
    ("Czy lubisz gotować? Jeśli tak, jakie jest Twoje popisowe danie?", "Do you like cooking? If so, what is your signature dish?"),
    ("Jakie są Twoje największe marzenia na przyszłość?", "What are your biggest dreams for the future?"),
    ("Jaka była najśmieszniejsza sytuacja, jaka Ci się przydarzyła?", "What was the funniest situation you've ever experienced?"),
    ("Czy wolisz deszcz czy słońce?", "Do you prefer rain or sunshine?"),
    ("Gdybyś mógł/mogła zamieszkać w dowolnym kraju, jaki byś wybrał/a?", "If you could live in any country, which one would you choose?"),
]


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

user_ids = set()

async def send_welcome_message(user_ids):
    mentions = " ".join([f"<@{user_id}>" for user_id in user_ids])
    
    
    selected_questions = random.sample(QUESTIONS, 4)
    
    
    welcome_message = f"""**Hej, {mentions} miło Was widzieć!**

Zechcecie opowiedzieć coś o sobie?

Nie musicie się do nich ograniczać, ale może poniższe pytania mogą w tym pomóc 🙂

1. Kim jesteś?
2. Co Cię pasjonuje?
3. Czym się zajmujesz?
4. Kto/co Cię do nas sprowadza?
5. {selected_questions[0][0]}

---

**Hey, nice to see you here! Would you like to introduce yourself?**

Those questions may help, but there's no need to limit yourself to them 🙂

1. Who are you?
2. What is your passion?
3. What do you do?
4. What/who brings you here?
5. {selected_questions[0][1]}"""

    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
        await webhook.send(content=welcome_message)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
def dummy(): pass  # placeholder for context
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.channel.id == SOURCE_CHANNEL_ID:
        user_ids.add(message.author.id)
        
        if len(user_ids) >= 3:
            # 80% chance to trigger Verifriend after every user >= 3
            if random.random() < 0.8:
                # Random delay between 5 minutes and 12 hours
                await asyncio.sleep(random.uniform(300, 43200))
                await send_welcome_message(user_ids)
                # Clear user_ids after sending the welcome message
                user_ids.clear()

    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx):
    global user_ids
    user_ids.clear()
    await ctx.send("User ID counter has been reset.")

bot.run(TOKEN)
