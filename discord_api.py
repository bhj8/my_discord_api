
# This example requires the 'message_content' intent.

import os

import discord
#读取当前工作目录下的env文件，获取token
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MY_DISCORD_TOJEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)#d反正这个token试一下就马上要改了，提交就提交吧


