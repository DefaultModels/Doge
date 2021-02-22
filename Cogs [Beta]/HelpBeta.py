import keep_alive
import discord
from discord.ext import commands
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
      em = discord.Embed(title = "Help",color = (0x95a5a6),description = "React with :moneybag: for currency commands \n React with :zany_face: for fun commands \n React with :crown: for premium commands")
      await ctx.send(embed = em)

      await em.add_reaction("💰")
      await em.add_reaction("👑")
      await em.add_reaction("🤪")

      def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) in ['️💰', '👑','🤪']

      try:
        reaction, user = await bot.wait_for('reaction_add', timeout=5, check=check)
    
        if reaction.emoji == '💰':
          em = discord.Embed(title = ":moneybag: Currency",value = "`cook` - Cook some cookies and sell them \n `beg` - Beg and get coins \n `farm` - Farm and sell the production for coins \n ~~`daily` - Get 1500 coins every day~~ \n `balance` - Shows you the amount of money you have \n `work` - Work and earn coins \n `postmemes` - Post memes on reddit to get ad money \n `search` - Look for some coins \n `slots` - Gamble to win coins (or lose)", inline=False)
          await ctx.send(embed = em)

        elif reaction.emoji == "👑":
          em = discord.Embed(title = ":crown: Premium",value = "~~`weekly` - Get 15000 coins every week~~", inline=False)
          await ctx.send(embed = em)

        elif reaction.emoji == "🤪":
          em = discord.Embed(title = ":crown: Premium",value = "~~`weekly` - Get 15000 coins every week~~", inline=False)
          await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Help(bot))