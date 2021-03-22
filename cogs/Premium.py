import discord
from discord.ext import commands

class Premium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def premium(self, ctx):
      em = discord.Embed(title = "Premium [Beta]",color = discord.Color.from_rgb(255,255,0), description = "Buy premium for exclusive commands, premium giveaways and donor role and giveaways for LIFE (In the official server)!")
      em.add_field(name="Commands", value="```Gig```")
      em.add_field(name="Features", value="```Anti-rob Shield```")
      em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/822959294504501268/ZzU5QyqU-removebg-preview.png")
      em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
      await ctx.send(embed = em)


def setup(bot):
  bot.add_cog(Premium(bot))