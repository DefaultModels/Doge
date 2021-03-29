from discord.ext import commands
from discord import Activity, ActivityType
import os
import discord
import json
from random import choice
import asyncio
import random

bot = commands.Bot(command_prefix="+", case_insensitive=True)

bot.remove_command('help')

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


# -------------------------------------------------

async def stocks():
	while True:
		channel = bot.get_channel(823969869095370852)
		global bitcoinstock
		global applestock
		global androidstock

		bitcoinstock = random.randint(40000, 60000)
		applestock = random.randint(10000, 20000)
		androidstock = random.randint(10000, 20000)

		BotMessage = await channel.send(
		    content=
		    f"<:Bitcoin:823980829914693652> Bitcoin Stock: {bitcoinstock} \n       ID: `btc` \n \n<:Android:824035438078853130> Android Stock: {androidstock} \n       ID: `android` \n \n<:Apple:824035438141505596> Apple: {applestock} \n       ID: `apple`"
		)
		await asyncio.sleep(60)
		await BotMessage.delete()


@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Streaming(
	    name=f"+help - {len(bot.guilds)} servers - dsc.gg/wumpusbot",
	    url="https://www.twitch.tv/defaultmodels"))
	print('Bot is online')
	await stocks()


token = os.environ['token']
bot.run(token)