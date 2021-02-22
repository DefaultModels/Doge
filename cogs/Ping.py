import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["delay"])
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Ping(bot))