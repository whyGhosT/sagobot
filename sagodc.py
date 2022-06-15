import discord
import os
import random
from discord.ext import commands
from yuh import randomsago, sesa, slol, kapak

sagotoken = ""

sago = commands.Bot(command_prefix="mf!")
sago.remove_command('help')

@sago.event
async def on_ready():
    await sago.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="mf! yardım | Kağıt Kesikleri OUT!"))
    print("Bot başarılı şekilde çalıştırıldı.")
    
@sago.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title=f"Yavaş ol. %.2f saniye sonra tekrar dene.." % error.retry_after)
        embed.set_author(name="SagoBot", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
        embed.set_footer(text="by wg-")
        await ctx.send(embed=embed)

@sago.command(aliases=['versiyon'])
@commands.cooldown(1,5,commands.BucketType.user)
async def version(ctx):
    embed=discord.Embed(title="Version : 0.3")
    embed.set_author(name="SagoBot", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
    embed.set_footer(text="by wg-")
    await ctx.send(embed=embed)
    
@sago.command(aliases=['help'])
@commands.cooldown(1,5,commands.BucketType.user)
async def yardım(ctx, *args):
    if "eğlence" in args:
        embed=discord.Embed()
        embed.set_author(name="Eğlence Komutları", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
        embed.add_field(name="mf!sagola", value="Sagolan!", inline=True)
        embed.add_field(name="mf!lirik", value="Cümle mühendisinden rastgele bir söz..", inline=True)
        embed.add_field(name="mf!sagodans", value="Sagoyu dans ettir..", inline=True)
        embed.set_footer(text="by wg-")
        await ctx.send(embed=embed)
    elif "müzik" in args:
        embed=discord.Embed()
        embed.set_author(name="Müzik Çok Yakında!", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
        embed.set_footer(text="by wg-")
        await ctx.send(embed=embed)
    elif "diğer" in args:
        embed=discord.Embed()
        embed.set_author(name="Diğer Komutlar", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
        embed.add_field(name="mf!versiyon", value="Botun sürümünü öğren.", inline=True)
        embed.add_field(name="mf!developer", value="Bu botu kim yaptı?", inline=True)
        embed.add_field(name="mf!ping", value="Botun pingini ölç.", inline=True)
        embed.set_footer(text="by wg-")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed()
        embed.set_author(name="Yardım", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
        embed.add_field(name="Eğlence Komutları İçin", value="mf!yardım eğlence", inline=True)
        embed.add_field(name="Müzik Komutları İçin", value="mf!yardım müzik", inline=True)
        embed.add_field(name="Diğer Komutlar İçin", value="mf!yardım diğer", inline=True)
        embed.set_footer(text="by wg-")
        await ctx.send(embed=embed)

        
@sago.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def developer(ctx):
    embed=discord.Embed()
    embed.set_author(name="by wg-", url="https://whyghost.github.io")
    embed.set_image(url="https://i.pinimg.com/originals/dc/a8/eb/dca8eb77a4b4788f1abb112b4ca4f773.jpg")
    await ctx.send(embed=embed)

@sago.command()
async def sagola(ctx):
@commands.cooldown(1,5,commands.BucketType.user)
    yuh = random.randint(1,2)
    if yuh == 1:
        abo = random.randint(75,217)
        embed=discord.Embed()
        embed.set_author(name="Sagolandın!", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
        embed.set_footer(text="by wg-")
        embed.set_image(url=f"https://galeri.bidibidi.com/albumler/galerim/11920/616/normal_Sagopa_({abo}).jpg")
        await ctx.send(embed=embed)
    else:
        ah = rastgelesago.copy()
        pu = random.choice(ah)
        embed=discord.Embed()
        embed.set_author(name="Sagolandın!", url="https://whyghost.github.io", icon_url="https://w0.peakpx.com/wallpaper/531/278/HD-wallpaper-sagopa-kajmer-turkce-rap-thumbnail.jpg")
        embed.set_footer(text="by wg-")
        embed.set_image(url=pu)
        await ctx.send(embed=embed)
        
@sago.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def lirik(ctx):
    randomxd = random.randint(0,90)
    zort = sesa.copy()
    zort2 = slol.copy()
    zort3 = kapak.copy()
    secbirini = zort[randomxd]
    secamk = zort2[randomxd]
    hadiamk = zort3[randomxd]
    embed=discord.Embed()
    embed.set_author(name=secbirini, url=secamk)
    embed.set_footer(text="by wg-")
    embed.set_image(url=hadiamk)
    yapistir = await ctx.send(embed=embed)
    up = '👍'
    down = '👎'
    await yapistir.add_reaction(up)
    await yapistir.add_reaction(down)
    
@sago.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def ping(ctx):
    ping = round (sago.latency * 1000)
    embed=discord.Embed()
    embed.set_author(name=f"Botun pingi : {ping}", url="https://whyghost.github.io")
    embed.set_footer(text="by wg-")
    await ctx.send(embed=embed)
    
@sago.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def sagodans(ctx):
    secbaqalim = random.randint(1,2)
    if secbaqalim == 1:
        ahh = rastgelesago.copy()
        xd = ahh[8]
        embed=discord.Embed()
        embed.set_author(name="SAGO DANS SAGO DANS SAGO DANS WAOOW", url="https://whyghost.github.io")
        embed.set_footer(text="by wg-")
        embed.set_image(url=xd)
        await ctx.send(embed=embed)
    else:
        ahh = rastgelesago.copy()
        xd = ahh[13]
        embed=discord.Embed()
        embed.set_author(name="SAGO DANS SAGO DANS SAGO DANS WAOOW", url="https://whyghost.github.io")
        embed.set_footer(text="by wg-")
        embed.set_image(url=xd)
        await ctx.send(embed=embed)

sago.run(sagotoken)