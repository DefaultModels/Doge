import discord
from discord.ext import commands
import json
import random
from discord import Activity, ActivityType
import asyncio

class Prestige(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def prestige(self, ctx):
      await open_account(ctx.author)
      user = ctx.author
      users = await get_bank_data()
      
      wallet_amt = users[str(user.id)]["wallet"]
      multi_amt = users[str(user.id)]["multi"]
      
      loss = 5000
      total = loss * multi_amt
      gain = random.randint(1, 5)

      if wallet_amt >= total:
        users[str(user.id)]["wallet"] -= total
        users[str(user.id)]["multi"] += gain

        await ctx.send(f"Congratulations! You have exchanged {total} coins for multipliers.")
      
      else:
        await ctx.send(f"You need {total} coins to prestige!")
      
      with open("mainbank.json","w") as f:
        json.dump(users,f)  
    
    @prestige.error
    async def prestige_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Chillax man. The default cooldown for this command is `5s`")

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
  bot.add_cog(Prestige(bot))