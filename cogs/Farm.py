import keep_alive
import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class Farm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def farm(self, ctx):
      await open_account(ctx.author)

      users = await get_bank_data()
    
      user = ctx.author
      multi_amt = users[str(user.id)]["multi"]
      earnings = random.randint(1, 50)
      total = earnings * multi_amt

      await ctx.send(f"You stole the eggs from the chickens! You sold the eggs for {total} coins!")

      users[str(user.id)]["wallet"] += total

      bankupgrade = 10
      users[str(user.id)]["bankmax"] += bankupgrade

      with open("mainbank.json","w") as f:
        json.dump(users,f)
    
    @farm.error
    async def farm_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("The farm is curently closed. The default cooldown for this coomand is `45s`.")

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
    bot.add_cog(Farm(bot))