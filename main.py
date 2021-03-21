import keep_alive
from discord.ext import commands
from discord import Activity, ActivityType
import os
import discord

bot = commands.Bot(command_prefix="+", case_insensitive=True)

bot.remove_command('help')

def is_any_user(ids):
    async def predicate(ctx):
        return ctx.author.id in ids
    return commands.check(predicate)

LIST_OF_PREMIUMS = [461301910289383436]

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name = f"+help - {len(bot.guilds)} servers - dsc.gg/wumpusbot", url = "https://www.twitch.tv/defaultmodels"))
  print('Bot is online')

for file in os.listdir("./cogs"): 
    if file.endswith(".py"): 
        name = file[:-3] 
        bot.load_extension(f"cogs.{name}")

@bot.command()
@commands.is_owner()
async def load(ctx, *, name: str):
    try:
        bot.load_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'"**{name}**" Cog loaded')

@bot.command()
@commands.is_owner()
async def reload(ctx, *, name: str):
    try:
        bot.reload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'"**{name}**" Cog reloaded')

@bot.command()
@commands.is_owner()
async def unload(ctx, *, name: str):
    try:
        bot.unload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'"**{name}**" Cog unloaded')

keep_alive.keep_alive()
bot.run('Nzg1MTYwMzgzNTYwMjg2MjQw.X8zzlw.1hFbOSTspGSltPRdhIQOHq8lcKw')
