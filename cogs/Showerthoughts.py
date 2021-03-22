import discord
from discord.ext import commands
import random
import praw

reddite = praw.Reddit(client_id='EvLPVk7GCoVgrQ',
                      client_secret='Y4NleCG1wpxY1Td_im812-zWIBM',
                      user_agent='somerandom',
                      username='pyUsagi')

class Showerthought(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def showerthought(self, ctx):
        subred = reddite.subreddit('showerthoughts')
        neewmeem = subred.hot(limit=100)
        lstmeem = list(neewmeem)
        randsub = random.choice(lstmeem)
        embed = discord.Embed(title=randsub.title,
                              url=randsub.url, color=discord.Color.from_rgb(47, 49, 54))
        embed.set_image(url=randsub.url)
        embed.set_footer(text=f'⬆️ {randsub.score} - 💬 {len(randsub.comments)} ')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Showerthought(bot))