import keep_alive
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
    
      earnings = random.randint(0, 200)


      await ctx.send(f"You posted a meme and earned {earnings} coins from the ads")

      users[str(user.id)]["wallet"] += earnings

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
    bot.add_cog(Postmemes(bot))