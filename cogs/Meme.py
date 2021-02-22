import discord
from discord.ext import commands
import random
import praw

reddite = praw.Reddit(client_id='EvLPVk7GCoVgrQ',
                      client_secret='Y4NleCG1wpxY1Td_im812-zWIBM',
                      user_agent='somerandom',
                      username='pyUsagi')

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def meme(self, ctx):
        subred = reddite.subreddit('memes')
        neewmeem = subred.hot(limit=100)
        lstmeem = list(neewmeem)
        randsub = random.choice(lstmeem)
        embed = discord.Embed(title=randsub.title,
                              description=f':arrow_up_small: {randsub.score} \n \n :speech_balloon: {len(randsub.comments)} ',
                              url=randsub.url, color=discord.Color.from_rgb(47, 49, 54))
        embed.set_image(url=randsub.url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Meme(bot))