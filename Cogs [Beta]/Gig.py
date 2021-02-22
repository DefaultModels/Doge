import keep_alive
import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')


class Gig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @is_any_user(LIST_OF_PREMIUMS)
    @commands.cooldown(1, 25, commands.BucketType.user)
    async def gig(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()

        user = ctx.author

        earnings = random.randrange(101)

        ee = "mowed a lawn", "washed windows", "babysitted a 4 year old (RIP)", "walked a dog", "painted a wall"

        await ctx.send(f"You {random.choice{ee}} and earned {earnings} coins!")

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @gig.error
    async def gig_cooldown(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                "No one needs you right now. The default cooldown for this coomand is `45s`."
            )


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 250
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return True


def setup(bot):
    bot.add_cog(Gig(bot))
