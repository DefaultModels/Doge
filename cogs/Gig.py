import keep_alive
import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class Gig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def gig(self, ctx):
      await open_account(ctx.author)

      users = await get_bank_data()
    
      user = ctx.author
      premium = users[str(user.id)]["premium"]
      multi_amt = users[str(user.id)]["multi"]

      earnings = random.randint(1, 50)
      total = earnings * multi_amt

      if premium == 1:
        await ctx.send(f"You got {total} coins!")

        users[str(user.id)]["wallet"] += total

        bankupgrade = 10
        users[str(user.id)]["bankmax"] += bankupgrade
        with open("mainbank.json","w") as f:
          json.dump(users,f)
        
      else:
        await ctx.send("You need premium to use this command!")
    
    @gig.error
    async def gig_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Whoa there buddy, you gotta wait before helping someone again. The default cooldown for this coomand is `30s`.")

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
    bot.add_cog(Gig(bot))