import discord
from discord.ext import commands
import random

class Dogerate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dogerate(self, ctx):
        dogelevel = random.randint(0, 100)
        await ctx.send(f"**{ctx.author.name}** is {dogelevel}% doge :dog:")

def setup(bot):
    bot.add_cog(Dogerate(bot))