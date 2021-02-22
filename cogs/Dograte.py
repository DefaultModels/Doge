import discord
from discord.ext import commands
import random

class Dograte(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def dograte(self, ctx):
      doglevel = random.randint(0, 100)
      await ctx.send(f"**{ctx.author.name}** is {doglevel}% dog :dog2:")

def setup(bot):
    bot.add_cog(Dograte(bot))