import os, random, requests, discord
from discord.ext import commands
from PIL import Image
from gsbl.stick_bug import StickBug

TOKEN = "PUT DISCORD TOKEN"

bot = commands.Bot(command_prefix='!')

@bot.command(name='stickbug', help='make image get stickbugged lol (attach image with command as text)')
async def stickbug(ctx):
    url = ctx.message.attachments[0].url
    print(url)
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        name = str(random.randint(1,2000))
        open(name + '.png', 'wb').write(r.content)
        sb = StickBug(Image.open(name + '.png'))
        print("Saved Image!")
        sb.save_video(name + '.mp4')
        print("Saving Video!")
        await ctx.send(file=discord.File(name + ".mp4"))
        os.remove(name + ".mp4")
        os.remove(name + ".png")

@bot.command(name='stickavatar', help='make an avatar a stickbug (mention user)')
async def stickavatar(ctx, user: discord.User):
    avatar_url = user.avatar_url
    print(avatar_url)
    r = requests.get(avatar_url, allow_redirects=True)
    if r.status_code == 200:
        name = str(random.randint(1,2000))
        open(name + '.png', 'wb').write(r.content)
        sb = StickBug(Image.open(name + '.png'))
        print("Saved Image!")
        sb.save_video(name + '.mp4')
        print("Saving Video!")
        await ctx.send(file=discord.File(name + ".mp4"))
        os.remove(name + ".mp4")
        os.remove(name + ".png")

bot.run(TOKEN)
