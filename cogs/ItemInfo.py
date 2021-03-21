import discord
from discord.ext import commands
import json
import random

class ItemInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx, category=None):
      await open_account(ctx.author)
      users = await get_bank_data()
      user = ctx.author
      
      with open("mainbank.json","w") as f:
        json.dump(users,f)
        
      if category == None:
        info = "To buy an item use: buy ID", "To get more info on an item use: shop ID"
        em = discord.Embed(title = "Shop", color = discord.Color.from_rgb(47, 49, 54))
        em.add_field(name = "Shop Items", value = "\n<:laptop:822951966975590421> **Laptop** — [2000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `laptop`", inline=False)
        em.set_footer(text=f"{random.choice(info)}")

        await ctx.send(embed = em)
        return


      if category == "laptop":
        laptop_amt = users[str(user.id)]["laptop"]
        em = discord.Embed(title = f"Laptop ({laptop_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Allows you to postmemes on reddit for coins. ```+postmemes```")
        em.add_field(name="Price:", value="`2000 coins`")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/822913208443994152/1447_laptop.png")

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
    bot.add_cog(ItemInfo(bot))
