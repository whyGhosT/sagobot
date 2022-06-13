import discord
import os
import random
from discord.ext import commands

sagotoken = ""

sago = commands.Bot(command_prefix="mf! "

@sago.event
async def on_ready():
    await sago.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Kağıt Kesikleri"))
    print("waow")

@sago.command(aliases=['versiyon']
@commands.cooldown(1,5,commands.BucketType.user)
async def version(ctx):
    await ctx.send("dur la")