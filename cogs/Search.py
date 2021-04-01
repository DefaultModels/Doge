import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def search(self, ctx):
      await open_account(ctx.author)

      users = await get_bank_data()
    
      user = ctx.author
    
      multi_amt = users[str(user.id)]["multi"]
      earnings = random.randint(50, 120)
      total = earnings * multi_amt

      action = "a dumpster","your closet","your bed","your car","the street","the pantry"
      
      deathreason = "You searched a dumpster and a homeless man gave you a expired sandwich which killed you!","You got run over by a car while searching the street!","You fell off a cliff while searching! Pay more attention next time!"

      deathrate = "die","die","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","live","die","live","live","live","live","live","live","live","live","live","live","die"
    
    
      fate = random.choice(deathrate)
      moneyloss = users[str(user.id)]["wallet"]

      if fate == "die":
        await ctx.send(f"{random.choice(deathreason)}")

        users[str(user.id)]["wallet"] -= moneyloss

      elif fate == "live":
        await ctx.send(f"You searched {random.choice(action)} and earned {total} coins!")

        users[str(user.id)]["wallet"] += total
    
      bankupgrade = 10
      users[str(user.id)]["bankmax"] += bankupgrade

      with open("mainbank.json","w") as f:
        json.dump(users,f)

    @search.error
    async def search_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Your still looking for a place to search! The default cooldown for this command is `45s`.")

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
    bot.add_cog(Search(bot))