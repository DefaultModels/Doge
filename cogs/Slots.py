import keep_alive
import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["gamble"])
    async def slots(self, ctx, bet = None):
      await open_account(ctx.author)

      users = await get_bank_data()
    
      user = ctx.author
  
      amount = int(bet)

      multi_amt = users[str(user.id)]["multi"]
      total = multi_amt * amount
      number_with_commas = "{:,}".format(total)
      number_with_commas_two = "{:,}".format(amount)
      markings = ":gem: | :gem: | :gem:",":gem: | :coin: | :gift:",":gift: | :moneybag: | :gem:",":moneybag: | :gem: | :coin:",":gem: | :moneybag: | :gem:",":coin: | :gift: | :gem:",":coin: | :moneybag: | :coin:",":gem: | :gem: | :gift:"


      selection = random.choice(markings)

      if selection == ":gem: | :gem: | :gem:":
        em = discord.Embed(title = f"**{ctx.author.name}' slots:**",color = (0x2ecc71),description = f"{selection} \n \n :postal_horn: You won {number_with_commas} coins! :postal_horn:")
        await ctx.send(embed = em)

        users[str(user.id)]["wallet"] += total

      elif selection  != ":gem: | :gem: | :gem:":
        em = discord.Embed(title = f"**{ctx.author.name}' slots:**",color = (0xe74c3c),description = f"{selection} \n \n :wastebasket: You lost your bet of {number_with_commas_two} coins. :wastebasket:")
        await ctx.send(embed = em)    

        users[str(user.id)]["wallet"] -= amount
    
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
    bot.add_cog(Slots(bot))