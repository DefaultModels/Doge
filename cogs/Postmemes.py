import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class Postmemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["pm"])
    @commands.cooldown(1, 35, commands.BucketType.user)
    async def postmemes(self, ctx):
      await open_account(ctx.author)

      users = await get_bank_data()
    
      user = ctx.author
      multi_amt = users[str(user.id)]["multi"]
      earnings = random.randint(0, 100)
      total = earnings * multi_amt
      laptopstatus = users[str(user.id)]["laptop"]
      event = random.randint(1, 20)

      if laptopstatus >= 1:
        if event == 20:
          await ctx.send("Your meme was so terrible your computer broke!")
          users[str(user.id)]["laptop"] -= 1
        
        else:
          await ctx.send(f"You posted a meme and earned {total} coins from the ads")

          users[str(user.id)]["wallet"] += total

        bankupgrade = 10
        users[str(user.id)]["bankmax"] += bankupgrade
        
      else: 
        await ctx.send("You need a laptop to post memes, go buy one from the shop.")
        
      with open("mainbank.json","w") as f:
        json.dump(users,f)  
    
    @postmemes.error
    async def work_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You're being rate limited by Reddit! The default cooldown for this command is `35s`.")

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
    bot.add_cog(Postmemes(bot))