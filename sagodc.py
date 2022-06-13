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
    embed=discord.Embed(title="SagoBot")
    embed.set_author(name="wg-", url="https://whyghost.github.io")
    embed.add_field(name="Version:", value="0.1", inline=False)
    embed.set_footer(text="by wg-")
    await ctx.send(embed=embed)