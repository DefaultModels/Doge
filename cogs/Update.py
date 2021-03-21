import discord
from discord.ext import commands

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["changelog"])
    async def update(self, ctx):
      em = discord.Embed(title = "Update",color = discord.Color.from_rgb(47, 49, 54), )
      em.add_field(name="UPDATE 1.2.2", value="**Commands:** \n<:Plus:823009473609072721> Withdraw \n<:Plus:823009473609072721> Deposit \n \n<:Settings:823004708699897886> **Update Notes:** \nBalance GUI was also updated to allow the new bank system. There's currently no way to buy bank storage space but an update regarding that will soon come. For now, bank space goes up when you play. If you die while searching, you lose all of your wallet money, not bank.")
      em.add_field(name="UPDATE 1.3.0", value="**Commands:** \n<:Plus:823009473609072721> Shop \n<:Plus:823009473609072721> Buy \n \n<:Settings:823004708699897886> **Update Notes:** \nThe postmemes command now requires a laptop which can be bought in the shop (`+shop`) using (`+buy laptop`). There's a 1/20 chance your laptop breaks.")
      em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823175485126082581/1_wy4fOE3UDRRylqzsrfaKMQ.png")
      em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
      await ctx.send(embed = em)


def setup(bot):
  bot.add_cog(Update(bot))