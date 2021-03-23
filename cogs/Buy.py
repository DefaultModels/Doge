import discord
from discord.ext import commands
import json

class Buy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buy(self, ctx, category=None):
      await open_account(ctx.author)
      users = await get_bank_data()
      user = ctx.author
      wallet_amt = users[str(user.id)]["wallet"]
        
      if category == None:
        await ctx.send("Please specify the item you would like to buy.")
        return

      if category == "laptop":
        if wallet_amt >= 2000:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = "You bought 1 laptop and you can now postmemes on reddit for coins. ```+postmemes```")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823539841089404988/1447_laptop.png")

          users[str(user.id)]["laptop"] += 1
          users[str(user.id)]["wallet"] -= 2000

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have enough money to buy a laptop!")
        return

      if category == "gun":
        if wallet_amt >= 5000:
          em = discord.Embed(title = "Transaction successful",color = discord.Color.from_rgb(47, 49, 54),description = "You bought 1 gun and you can now rob other players for coins. ```+rob MENTION```")
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823900235649777684/1426_pistol.png")

          users[str(user.id)]["gun"] += 1
          users[str(user.id)]["wallet"] -= 5000

          await ctx.send(embed = em)

          with open("mainbank.json","w") as f:
            json.dump(users,f)
          
        
        else:
          await ctx.send("You don't have enough money to buy a gun!")
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
