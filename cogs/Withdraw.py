import discord
from discord.ext import commands
import json
import random
from discord import Activity, ActivityType
import asyncio

class Withdraw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["with"])
    async def withdraw(self, ctx, amount = 0):
      await open_account(ctx.author)
      user = ctx.author
      users = await get_bank_data()

      bank_amt = users[str(user.id)]["bank"]

      if amount <= bank_amt:

        users[str(user.id)]["bank"] -= amount
        users[str(user.id)]["wallet"] += amount
        number_with_commas = "{:,}".format(amount)

        await ctx.send(f"{ctx.author.mention}, you successfully withdrawed {number_with_commas} coins!")
      
      else:
        await ctx.send(f"{ctx.author.mention}, you don't have enough in your bank to withdraw that much!")
      
      with open("mainbank.json","w") as f:
        json.dump(users,f)
      


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
  bot.add_cog(Withdraw(bot))