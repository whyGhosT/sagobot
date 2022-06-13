import discord
import os
import random
from discord.ext import commands

sagotoken = ""

sago = commands.Bot(command_prefix="mf! ")

@sago.event
async def on_ready():
    await sago.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="mf! yardım | Kağıt Kesikleri OUT!"))
    print("Bot başarılı şekilde çalıştırıldı.")
    
@sago.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title=f"Yavaş ol. %.2f saniye sonra tekrar dene.." % error.retry_after)
        embed.set_author(name="SagoBot", url="https://whyghost.github.io")
        embed.set_footer(text="by wg-")
        await ctx.send(embed=embed)

@sago.command(aliases=['versiyon'])
@commands.cooldown(1,5,commands.BucketType.user)
async def version(ctx):
    embed=discord.Embed(title="Version : 0.1")
    embed.set_author(name="SagoBot", url="https://whyghost.github.io")
    embed.set_footer(text="by wg-")
    await ctx.send(embed=embed)

sago.run(sagotoken)