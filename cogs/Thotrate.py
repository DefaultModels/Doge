import discord
from discord.ext import commands
import random

class Thotrate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thotrate(self, ctx):
      thotlevel = random.randint(0, 100)
      await ctx.send(f"**{ctx.author.name}** is {thotlevel}% thot")

def setup(bot):
    bot.add_cog(Thotrate(bot))