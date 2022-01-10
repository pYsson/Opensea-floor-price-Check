import requests
import json
import discord
from discord.ext import commands
from bs4 import BeautifulSoup as soup
import sendWebhook, bithumb

Client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
footer_img = "https://pbs.twimg.com/profile_images/1196129571914969088/gOsdiF6Z_400x400.jpg"

TOKEN = ''

@client.event
async def on_ready():
    global TOKEN
    print("Check floor price")

@client.event
async def on_message(message):      
    if message.content.startswith('!floor'):
      messageSplit = message.content.split(' ')
      nft_name = str(messageSplit[1])
      channel = message.channel
      
      eth, klay = bithumb.extract()
      
      with open('opensea.json', 'r') as f:
        site = json.load(f)
      
      try:  
        embed = sendWebhook.parseEmbed(site[nft_name], eth, klay)
        await channel.send(embed=embed)
      except:
        embed = discord.Embed(title="**등록되지 않은 사이트입니다.**", description="", color=0x000000)
        embed.set_thumbnail(url=footer_img)
        embed.set_footer(text="Powered By pYsson#3604", icon_url=footer_img)
        await channel.send(embed=embed)

if __name__ == '__main__':
  while True:
    if len(TOKEN) == 0:
      TOKEN = input("Type your discord bot token: ")
    else:
      break
    
  client.run(TOKEN)