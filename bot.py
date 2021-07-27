from check import check_img
from PIL import Image
import discord
import sys
import requests
import io

def get_img(src):
    response = requests.get(src)
    image_bytes = io.BytesIO(response.content)
    img = Image.open(image_bytes).convert("RGB")
    return img

img_ext = ["png", "jpg", "jpeg", "webp", "gif", "bmp", "ico", "tiff"]

client = discord.Client()   

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith("meow"):
        await message.channel.send("meow")
    for a in message.attachments:
        if a.filename.lower().split('.')[-1] in img_ext:
            img = get_img(a.url)
            p = check_img(img)*100
            await message.reply(str(p)+"% cat!")

client.run(sys.argv[1])