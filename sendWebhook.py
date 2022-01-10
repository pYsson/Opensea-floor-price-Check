import json
import requests
import discord

footer_img = "https://cdn.discordapp.com/attachments/839743332891885588/929645365479759882/pylogo.png"
headers = {"Accept": "application/json"}

def parseEmbed(data, eth, klay):
  try:
    response = requests.request("GET", data['apiUrl'], headers=headers)
    stats = json.loads(response.text)['stats']
    fp = round(stats['floor_price'], 3)
    krwprice = int(fp * eth)
    klayPrice = krwprice // klay
    
    supply = int(stats['total_supply'])
    owner = stats['num_owners']
    oneV = round(stats['one_day_volume'], 3)
    oneS = int(stats['one_day_sales'])
    
    embed = discord.Embed(title=data['name'], description="", url=data['url'], color=0x000000)
    embed.add_field(name="**총 발행량**", value="{:,}".format(supply) + " 개", inline=False)
    embed.add_field(name="**홀더 수**", value="{:,}".format(owner) + " 명", inline=False)
    embed.add_field(name="**일일 거래량**", value="{:,}".format(oneV) + " ETH")
    embed.add_field(name="**일일 거래건수**", value="{:,}".format(oneS) + " 건" , inline=True)
    embed.add_field(name="**바닥 가격 (ETH)**", value="{:,}".format(fp) + " ETH", inline=False)
    embed.add_field(name="**바닥 가격 (KLAY)**", value="{:,}".format(klayPrice) + " KLAY", inline=False)
    embed.add_field(name="**바닥 가격 (KRW)**", value="{:,}".format(krwprice) + " 원", inline=False)
    embed.set_thumbnail(url=data['logo'])
    embed.set_footer(text="Powered By pYsson#3604", icon_url=footer_img)
  except:
    embed = discord.Embed(title="**Failed to get Info!**", description="", color=0x000000)
    embed.set_thumbnail(url=footer_img)
    embed.set_footer(text="Powered By pYsson#3604", icon_url=footer_img)
    
  return embed