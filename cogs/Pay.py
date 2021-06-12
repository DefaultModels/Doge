import discord
from discord.ext import commands
import json
import random

class Pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pay(self, ctx, mention: discord.User, amount = 0):
      await open_account(ctx.author)
      await open_account(mention)
      user = ctx.author
      users = await get_bank_data()

      total = amount

      users[str(user.id)]["wallet"] -= total
      users[str(mention.id)]["wallet"] += total

      await ctx.send(f"{ctx.author.mention}, you gave {total} coins to {mention}")

      with open("mainbank.json","w") as f:
        json.dump(users,f)  
    
    @pay.error
    async def pay_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You're going on a giving rampage. The default cooldown for this command is `5s`.")


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
    bot.add_cog(Pay(bot))
      