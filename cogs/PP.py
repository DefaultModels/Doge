import keep_alive
import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class PP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pp(ctx):

      size = "=","==","===","====","=====","======","=======","========"


      await ctx.send(f"**{ctx.author.name}'s PP:** 8{random.choice(size)}D")

def setup(bot):
    bot.add_cog(PP(bot))