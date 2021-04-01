import discord
from discord.ext import commands
import json
import main

class Buy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buy(self, ctx, category=None, amount=1):
      await open_account(ctx.author)
      users = await get_bank_data()
      user = ctx.author
      wallet_amt = users[str(user.id)]["wallet"]

      if category == None:
        await ctx.send("Please specify the item you would like to buy.")
        return

      if category == "laptop":
        if wallet_amt >= amount * 2000:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You bought {amount} laptops and you can now postmemes on reddit for coins. ```+postmemes```")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823539841089404988/1447_laptop.png")

          users[str(user.id)]["laptop"] += amount
          users[str(user.id)]["wallet"] -= amount * 2000

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send(f"You don't have enough money to buy {amount} laptops!")
        return

      if category == "gun":
        if wallet_amt >= amount * 5000:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You bought {amount} guns and you can now rob other players for coins. ```+rob MENTION```")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823900235649777684/1426_pistol.png")

          users[str(user.id)]["gun"] += amount
          users[str(user.id)]["wallet"] -= amount * 5000

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send(f"You don't have enough money to buy {amount} guns!")
        return

      if category == "coin":
        if wallet_amt >= amount * 500000:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You bought {amount} doge coins.")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/826907667909967892/Untitled_design__3_-removebg-preview.png")

          users[str(user.id)]["coin"] += amount
          users[str(user.id)]["wallet"] -= amount * 500000

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send(f"You don't have enough money to buy {amount} coins!")
        return

      if category == "medal":
        if wallet_amt >= amount * 1000000:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You bought {amount} doge medals.")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/826907664335241216/Untitled_design__2_-removebg-preview.png")

          users[str(user.id)]["medal"] += amount
          users[str(user.id)]["wallet"] -= amount * 1000000

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send(f"You don't have enough money to buy {amount} doge medals!")
        return

      if category == "doge":
        if wallet_amt >= amount * main.bitcoinstock:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You bought {amount} dogecoin for {amount * main.bitcoinstock} coins, sell on the stock market when you see profit. ```+sell doge```")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/827206454648897576/dogecoin-cryptocurrency-dash-digital-currency-doge-removebg-preview.png")

          users[str(user.id)]["btc"] += amount
          users[str(user.id)]["wallet"] -= amount * main.bitcoinstock

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have enough money to buy that much dogecoin with the current stock prices!")
        return   

      if category == "apple":
        if wallet_amt >= amount * main.applestock:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You bought {amount} apple stock for {amount * main.applestock} coins, sell it on the stock market when you see profit. ```+sell apple```")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/824035108972658728/1515_phone_with_apple.png")

          users[str(user.id)]["apple"] += amount
          users[str(user.id)]["wallet"] -= amount * main.applestock

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have enough money to buy that much apple stock with the current stock prices!")
        return   

      if category == "android":
        if wallet_amt >= amount * main.androidstock:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = f"You bought {amount} android stock for {amount * main.androidstock} coins, sell it on the stock market when you see profit. ```+sell android```")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/824035104258261022/1546_phone_with_android.png")

          users[str(user.id)]["android"] += amount
          users[str(user.id)]["wallet"] -= amount * main.androidstock

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have enough money to buy that much android stocks with the current stock prices!")
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
    bot.add_cog(Buy(bot))
