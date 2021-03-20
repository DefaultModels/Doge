import discord
from discord.ext import commands
import random

class Gayrate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gayrate(self, ctx):
      gaylevel = random.randint(0, 100)
      await ctx.send(f"**{ctx.author.name}** is {gaylevel}% gay :rainbow_flag:")

def setup(bot):
    bot.add_cog(Gayrate(bot))