import discord
from discord.ext import commands
import json

class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["inv"])
    async def inventory(self, ctx, mention: discord.User = None):
      await open_account(ctx.author)
      user = ctx.author
      users = await get_bank_data()

      if mention == None:
        guns = users[str(user.id)]["gun"]
        laptops = users[str(user.id)]["laptop"]
        coins = users[str(user.id)]["coin"]
        medals = users[str(user.id)]["medal"]

        guns = "{:,}".format(guns)
        laptops = "{:,}".format(laptops)
        medals = "{:,}".format(medals)
        coins = "{:,}".format(coins)
        
        pfp = user.avatar_url
        em = discord.Embed(title = f"{ctx.author.name}' Inventory",color = discord.Color.from_rgb(47, 49, 54), description = f"<:laptop:822951966975590421> Laptop — {laptops} \n<:gun:823900537291800626> Gun — {guns} \n<:DogeCoin:826907590650363954> Doge Coin — {coins} \n<:DogeMedal:826907545716392037> Doge Medal — {medals}")
        em.set_thumbnail(url=pfp)
        em.set_footer(text = "To view more info on an item use +shop ITEM_ID")
        await ctx.send(embed = em)

      else:
        await open_account(mention)
        guns = users[str(mention.id)]["gun"]
        laptops = users[str(mention.id)]["laptop"]
        coins = users[str(mention.id)]["coin"]
        medals = users[str(mention.id)]["medal"]

        guns = "{:,}".format(guns)
        laptops = "{:,}".format(laptops)
        medals = "{:,}".format(medals)
        coins = "{:,}".format(coins)

        pfp = mention.avatar_url
        em = discord.Embed(title = f"{mention}' Inventory",color = discord.Color.from_rgb(47, 49, 54), description = f"<:laptop:822951966975590421> Laptop — {laptops} \n<:gun:823900537291800626> Gun — {guns} \n<:DogeCoin:826907590650363954> Doge Coin — {coins} \n<:DogeMedal:826907545716392037> Doge Medal — {medals}")
        em.set_footer(text = "To view more info on an item use +shop ITEM_ID")
        em.set_thumbnail(url=pfp)
        await ctx.send(embed = em)

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
  bot.add_cog(Inventory(bot))
