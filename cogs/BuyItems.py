import discord
from discord.ext import commands
import json

class BuyItems(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buy(self, ctx, category=None, amount=1):
      users = await get_bank_data()
    
      user = ctx.author

      wallet_amt = users[str(user.id)]["wallet"]
      add_item = amount
      laptop_price = 5000

      if category == None:
        await ctx.send("You must specify the item you want to buy.")
        return

      if category == "laptop":
        if wallet_amt >= 5000:
          
          total_price = laptop_price * amount
          total_commas = "{:,}".format(total_price)

          users[str(user.id)]["wallet"] -= total_price
          users[str(user.id)]["laptop"] += add_item

          await ctx.send(f"You successfully bought {str(add_item)} for {total_commas}")
          return

        else:
          ctx.send("You don't have enought money to buy a laptop!")
          return 
        return
    
      with open("mainbank.json","w") as f:
        json.dump(users,f)  

async def open_account(user):
  
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 250
    users[str(user.id)]["multi"] = 2
    users[str(user.id)]["laptop"] = 0
    
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
    bot.add_cog(BuyItems(bot))
