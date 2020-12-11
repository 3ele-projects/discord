import discord
import subprocess

# discord client
client = discord.Client()


# create a new event
@client.event
async def on_ready():
     print("BOOP BEEP BOOP SQUEEE!")
     print("(Bot Ready)")


# listen for specific messages
@client.event
async def on_message(message):

    if message.content.startswith("/wget"):
        if message.channel == 'DMChannel': 
           subprocess.run('ls')
           removed = message.content.replace("/wget ", "")
           subprocess.run('wget example.com')
           print (removed)
           await message.channel.send(removed)
     #   await buggy = subprocess.run('dig +short stackoverflow.com')
    if message.content.startswith("/wp"):
     
           removed = message.content.replace("/wp ", "wp ")
           removed = removed.replace("-", ",-")
 
           result = subprocess.run([removed], stdout=subprocess.PIPE)

           await message.channel.send(result.stdout.decode())


# run the bot
bot = ""
client.run(bot)

