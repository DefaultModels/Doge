import discord
from discord.ext import commands
import json
import main

class Sell(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sell(self, ctx, category=None, amount=1):
      await open_account(ctx.author)
      users = await get_bank_data()
      user = ctx.author
      laptop_amt = users[str(user.id)]["laptop"]
      gun_amt = users[str(user.id)]["gun"]
      btc_amt = users[str(user.id)]["btc"]
      apple_amt = users[str(user.id)]["apple"]
      android_amt = users[str(user.id)]["android"]
      if category == None:
        await ctx.send("Please specify the item you would like to buy.")
        return

      if category == "laptop":
        if laptop_amt >= amount:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You sold {amount} laptop for {amount * 1000} coins.")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823539841089404988/1447_laptop.png")

          users[str(user.id)]["laptop"] -= amount
          users[str(user.id)]["wallet"] += amount * 1000

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have that many laptops, you can't sell them!")
        return

      if category == "gun":
        if gun_amt >= amount:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You sold {amount} guns for {amount * 2500} coins.")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823900235649777684/1426_pistol.png")

          users[str(user.id)]["gun"] -= amount
          users[str(user.id)]["wallet"] += amount * 2500

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have that many guns, you can't sell them!")
        return

      if category == "doge":
        if btc_amt >= amount:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You sold {amount} bitcoin for {amount * main.bitcoinstock} coins.")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/827206454648897576/dogecoin-cryptocurrency-dash-digital-currency-doge-removebg-preview.png")

          users[str(user.id)]["btc"] -= amount
          users[str(user.id)]["wallet"] += amount * main.bitcoinstock

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have that many dogecoins, you can't sell them!")
        return
    
      if category == "apple":
        if apple_amt >= amount:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You sold {amount} apple stock for {amount * main.applestock} coins.")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/824035108972658728/1515_phone_with_apple.png")

          users[str(user.id)]["apple"] -=amount
          users[str(user.id)]["wallet"] += amount * main.applestock

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have that many apple stock, you can't sell them!")
        return

      if category == "android":
        if android_amt >= amount:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You sold {amount} android stock for {amount * main.androidstock} coins.")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/824035104258261022/1546_phone_with_android.png")

          users[str(user.id)]["android"] -= amount
          users[str(user.id)]["wallet"] += amount * main.androidstock

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have that many android stocks, you can't sell them!")
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
    users[str(user.id)]["medal"] = 0
    users[str(user.id)]["coin"] = 0 
    

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
    bot.add_cog(Sell(bot))
