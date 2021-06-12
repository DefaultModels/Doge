import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class Ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["8ball"])
    async def ball(self, ctx):

      response = "Yes","No","Probably","Very doubtful", "I don't answer bitches", "Maybe?"

      await ctx.send(f"**:8ball: Answer:** {random.choice(response)}")

def setup(bot):
    bot.add_cog(Ball(bot))