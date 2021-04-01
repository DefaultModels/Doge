import discord
from discord.ext import commands
import main
import json
class Stock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stock(self, ctx, category=None):
      users = await get_bank_data()
    
      user = ctx.author
    
      btc_amt = users[str(user.id)]["btc"]
      apple_amt = users[str(user.id)]["apple"]
      android_amt = users[str(user.id)]["android"]

      if category == None:
        em = discord.Embed(title = "Stocks",color = discord.Color.from_rgb(47, 49, 54),description = f"**Amount Of Stocks Owned:** {btc_amt + android_amt + apple_amt} \n **Total Current Sale/Buy Price:** {main.bitcoinstock + main.applestock + main.androidstock} coins \n**Total Inventory Value:** {btc_amt * main.bitcoinstock + apple_amt * main.applestock + android_amt * main.androidstock} \n ")
        em.set_thumbnail(url="https://compote.slate.com/images/926e5009-c10a-48fe-b90e-fa0760f82fcd.png?width=1200&rect=680x453&offset=0x30")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "doge":
        em = discord.Embed(title = "Dogecoin",color = discord.Color.from_rgb(47, 49, 54),description = f"Buy dogecoin from the stock market and sell it. [What is dogecoin?](https://en.wikipedia.org/wiki/Dogecoin). \n \n **Amount Owned:** {btc_amt} \n **Current Sale/Buy Price:** {main.bitcoinstock} coins \n**Inventory Value:** {btc_amt * main.bitcoinstock} \n ")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/827206454648897576/dogecoin-cryptocurrency-dash-digital-currency-doge-removebg-preview.png")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "apple":
        em = discord.Embed(title = "Apple Stock",color = discord.Color.from_rgb(47, 49, 54),description = f"Buy apple from the stock market and sell it. [What is apple?](https://en.wikipedia.org/wiki/Apple_Inc.). \n \n **Amount Owned:** {apple_amt} \n **Current Sale/Buy Price:** {main.bitcoinstock} coins \n**Inventory Value:** {apple_amt * main.applestock} \n ")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/824035108972658728/1515_phone_with_apple.png")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "android":
        em = discord.Embed(title = "Android Stock",color = discord.Color.from_rgb(47, 49, 54),description = f"Buy android from the stock market and sell it. [What is android?](https://en.wikipedia.org/wiki/Android_(operating_system)). \n \n **Amount Owned:** {android_amt} \n **Current Sale/Buy Price:** {main.androidstock} coins \n**Inventory Value:** {apple_amt * main.androidstock} \n ")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/824035104258261022/1546_phone_with_android.png")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return
async def open_account(user):
  
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 250
    users[str(user.id)]["multi"] = 2
    users[str(user.id)]["bank"] = 0
    users[str(user.id)]["bankmax"] = 100
    users[str(user.id)]["laptop"] = 0
    users[str(user.id)]["premium"] = 0 
    users[str(user.id)]["gun"] = 0 
    users[str(user.id)]["btc"] = 0 
    users[str(user.id)]["apple"] = 0     
    users[str(user.id)]["android"] = 0 
 
    
    
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
      users = json.load(f)

    return users


async def update_bank(user,change = 0,mode = "wallet"):
  users = await get_bank_data()
  
  users[str(user.id)][mode] += change

  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True

def setup(bot):
    bot.add_cog(Stock(bot))