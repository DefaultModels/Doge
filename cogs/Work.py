import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

class Work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["job"])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def work(self, ctx):
      await open_account(ctx.author)

      users = await get_bank_data()
    
      user = ctx.author
      multi_amt = users[str(user.id)]["multi"]
      earnings = random.randint(1000, 1500)
      total = earnings * multi_amt
      number_with_commas = "{:,}".format(total)

      randomjob = "McDonalds Cashier","UPS Driver","Teacher","Secretary","Doge developer"


      await ctx.send(f"You worked as a {random.choice(randomjob)} for one hour and earned {number_with_commas} coins!")

      users[str(user.id)]["wallet"] += total

      bankupgrade = 10
      users[str(user.id)]["bankmax"] += bankupgrade

      with open("mainbank.json","w") as f:
        json.dump(users,f)
    
    @work.error
    async def work_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Stop trying to be the employee of the month! The default cooldown for this command is `1h`.")

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
    bot.add_cog(Work(bot))