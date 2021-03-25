import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio


class PP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pp(self, ctx, mention: discord.User = None):
      
      if mention == None:
        size = "=","==","===","====","=====","======","=======","========"
        await ctx.send(f"**{ctx.author.name}'s PP:** 8{random.choice(size)}D")

      else: 
        size = "=","==","===","====","=====","======","=======","========"
        await ctx.send(f"**{mention}'s PP:** 8{random.choice(size)}D")

def setup(bot):
    bot.add_cog(PP(bot))