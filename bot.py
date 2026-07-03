import discord
import random 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def cool(ctx):
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def meme(ctx):
    images = os.listdir("images(MODUL 2)")

    img_name = random.choice(images)

    with open("images(MODUL 2)/" + img_name, "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image():
    url = "https://randomfox.ca/floof/"
    res = requests.get(url)
    data = res.json()
    return data["image"]

@bot.command()
async def fox(ctx):
    await ctx.send(get_fox_image())

@bot.command()
async def fakta(ctx):
    await ctx.send(get_fakta())

@bot.command()
async def tips(ctx):
    await ctx.send(get_tips())

@bot.command()
async def recycle(ctx):
    await ctx.send(get_recycle())

@bot.command()
async def laut(ctx):
    await ctx.send(get_laut())

bot.run("TOKEN")
