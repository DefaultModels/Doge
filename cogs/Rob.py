import discord
from discord.ext import commands
import json
import random

class Rob(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def rob(self, ctx, mention: discord.User):
      await open_account(ctx.author)
      user = ctx.author
      users = await get_bank_data()
      event = random.randint(1, 2)
      target_wallet_amt = users[str(mention.id)]["wallet"]
      wallet_amt = users[str(user.id)]["wallet"]
      target_premium = users[str(mention.id)]["premium"]
      payout = random.randint(1000, target_wallet_amt)
      gun = users[str(user.id)]["gun"]

      if gun >= 1:
        if wallet_amt >= 2000:
          if target_wallet_amt >= 1000:
            if target_premium == 1:
              await ctx.send("Looks like the person you tried to rob has a shield enabled.")

            else:
              if event == 1:
                await ctx.send(f"{ctx.author.mention}, you robbed {mention} for {payout} coins")

                users[str(user.id)]["wallet"] += payout
                users[str(mention.id)]["wallet"] -= payout

              elif event == 2:
                loss = payout
                await ctx.send(f"{ctx.author.mention}, you were caught by {mention} and had to pay a {loss} coin fine.")

                users[str(user.id)]["wallet"] -= loss
                users[str(mention.id)]["wallet"] += loss

              with open("mainbank.json","w") as f:
                json.dump(users,f)

          else:
            await ctx.send("The player you mentioned has less than 1000 coins in their wallet, you cannot rob them.")
        else:
          await ctx.send("You need to have atleast 2000 coins in your wallet to rob someone!")
      else:
        await ctx.send("You need to own a gun to rob someone!")
    
    @rob.error
    async def rob_cooldown(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Chill, the cops are going to get you if you go crazy. The default cooldown for this command is `10mins`.")


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
    bot.add_cog(Rob(bot))
      