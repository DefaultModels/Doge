import discord
from discord.ext import commands

class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["sc"])
    async def botinfo(self, ctx):
      em = discord.Embed(title = "Bot Info",color = discord.Color.from_rgb(47, 49, 54))
      em.add_field(name="Ping", value=f"{round(self.bot.latency * 1000)}ms")
      em.add_field(name="Server count", value=f"{len(self.bot.guilds)} guilds")
      em.add_field(name="Developer", value="<@461301910289383436>", inline=False)
      em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/827211872422985798/8563_dogefluffy.png")
      await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Botinfo(bot))