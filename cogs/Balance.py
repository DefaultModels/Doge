import keep_alive
import discord
from discord.ext import commands
import json
import random
from discord import Activity, ActivityType
import asyncio

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["bal"])
    async def balance(self, ctx):
      await open_account(ctx.author)
      user = ctx.author
      users = await get_bank_data()

      wallet_amt = users[str(user.id)]["wallet"]
      bank_amt = users[str(user.id)]["bank"]
      bankmax_amt = users[str(user.id)]["bankmax"]

      wallet_with_commas = "{:,}".format(wallet_amt)
      bank_with_commas = "{:,}".format(bank_amt)
      bankmax_with_commas = "{:,}".format(bankmax_amt)

      em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.from_rgb(47, 49, 54), description = f"**Wallet:** {wallet_with_commas} coins \n**Bank:** {bank_with_commas} / {bankmax_with_commas} coins")
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
  bot.add_cog(Balance(bot))

    