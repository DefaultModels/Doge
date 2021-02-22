import keep_alive
import discord
from discord.ext import commands, tasks
import json
import random
from discord import Activity, ActivityType
import asyncio

bot = commands.Bot(command_prefix='+')

class Roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["insult"])
    async def roast(self, ctx):

      roast = "Y'know, I don't want another person being blinded by looking in the mirror.","Saw your mom confirm fake news, then i took my schrizophenia pills.","I only friend request ugly people. (Incoming Friend Request)","If you think im stupid, please look in the mirror.","Youre as useless as the -ueue- in queue.","If i had a face like yours, i would sue my parents.","I'd slap you, but that'll be animal abuse.","How many wrinkles does an asshole have? Smile, ill count them.","You're like the top piece of bread, everyone touches you but nobody wants you.","If you were a cookie, you'd be a whoreo.","The trash gets picked up tommorow, be ready.","Hey, train wreck. This isn't your station.","I'd unplug your life support to charge my phone.","You look like something i drew with my left hand.","You're so shitty that the toilet is jealous.","If zombies chase us, im tripping you.","You don't have to tell us you're a vegan, we can all tell","I'd love to stay and chat but I'd rather have type-2 diabetes","I would challenge you to a battle of wits, but it seems you come unarmed","Bards will chant parables of your legendary stupidity for centuries","You know, one of the many, many things that confuses me about you is that you remain unmurdered","My phone battery lasts longer than your relationships","It’s a shame you can’t Photoshop your personality","My middle finger gets a boner every time I see you","If I had a face like yours I’d sue my parents","I’d smack you, but that would be animal abuse","You’re so fat you could sell shade","You are proof that evolution can go in reverse","Learn from your parent's mistake... Use birth control","The smartest thing that ever came out of your mouth was a P_nis","Man you have more faces than Mt. Rushmore","You're entitled to your incorrect opinion!","Whoever told you to be yourself gave you really bad advice","I didn't change, I grew up you should try it sometime.","You sound reasonable, time to up my medication.","90% of your -beauty- can be removed with Kleenex","My hair straightener is hotter than you","I'd smack you, but that'd be animal abuse.","Hey I found your nose, it's on my business again.","Everyone brings happiness to a room, you just do it when you leave.","I'd like to explain it to you, but I left my English-To-Dumbass Dictionary at home.","If laughter is the best medicine, your face must be curing the world.","You're so ugly you scare the crap out of the toilet","The only way you'll ever get laid is by crawling up a chickens ass and waiting.","You're so fake Barbie is jealous.","If I wanted to kill myself, I'd climb your ego and jump to your IQ","Roses are red, violets are blue (or violet), God made me pretty, What happened to you?","Some babies are dropped on their heads, but you were clearly thrown at a wall!","Stop tryna be a smartass, you're clearly not smart.","Have you been shopping lately? They sell lives, you should go get one!","Oh a thought crossed your mind? Must've been a long and lonely journey..."


      await ctx.send(f"{random.choice(roast)}")

def setup(bot):
    bot.add_cog(Roast(bot))