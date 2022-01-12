import requests
import json
import discord
from discord.ext import commands
from bs4 import BeautifulSoup as soup
import sendWebhook, bithumb, openseaAdd

Client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
footer_img = "https://cdn.discordapp.com/attachments/839743332891885588/929645365479759882/pylogo.png"

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
    
    if message.content.startswith('!fadd'):
      messageSplit = message.content.split(' ')
      nickname = str(messageSplit[1])
      url = str(messageSplit[2])
      channel = message.channel
      
      tf = openseaAdd.addSite(nickname, url)
      
      if tf == True:
        embed = discord.Embed(title="**사이트가 등록되었습니다.**", description="", color=0x000000)
        embed.set_thumbnail(url=footer_img)
        embed.set_footer(text="Powered By pYsson#3604", icon_url=footer_img)
        await channel.send(embed=embed)
      else:
        embed = discord.Embed(title="**사이트 등록에 실패하였습니다!**", description="", color=0x000000)
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