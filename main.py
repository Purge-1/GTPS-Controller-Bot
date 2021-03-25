#This is a complete make and duplicate of ifanps is contoller
# Credit: iFanps
import discord
from discord.ext import commands
from discord import Client
import os, psutil
from datetime import datetime #All the imports
import random
from PIL import Image
from io import BytesIO #pip install pillow

token = 'token here'
prefix = '!'

client = commands.Bot(command_prefix=prefix)


client.remove_command('help')

Client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f"Prefix >> [{prefix}]"))
	
@client.event
async def on_message(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    boost = Image.open("boost.png")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read()) #You need this https://cdn.discordapp.com/attachments/751125832088682518/824380999722729512/boost.png
    pfp = Image.open(data)

    pfp = pfp.resize((173,159)) #519 x 110


    boost.paste(pfp, (605,18))

    boost.save("boostcard.png")
    boostmessage = discord.MessageType.premium_guild_subscription
    if boostmessage == True:
        await ctx.send(file = discord.File("boostcard.png"))	

@client.command()
async def status(ctx):
	for proc in psutil.process_iter():
		if 'server' in proc.name():
			await ctx.send("Server is now up!")
			break;
		else:
			if 'server' not in proc.name():
				await ctx.send("Server is now down.")


@client.command()
async def online(ctx):
	player = open('online.txt').readlines()
	await ctx.send(f"{listplayer} Accounts created.")

@client.command()
async def player(ctx):
	listplayer = len(os.listdir('players'))
	await ctx.send(f"{listplayer} Account created")

@client.command()
async def start(ctx):
	os.system(r'"server.exe')
	await ctx.send("Your server is up now.")

@client.command()
async def stop(ctx): # iFanp's is stop command.
    gabut = os.system("taskkill /f /im Your enet server.exe")
    if gabut == True:
        await ctx.send("Your server is Down")

@client.command()
async def world(ctx):
	listworld = len(os.listdir('worlds'))
	await ctx.send(f"{listworld} Created for now on.")

@client.command()
async def givegem(ctx, args1, args2):
	task1 = open(f'C://yourfoldergems69\\{args1}.json', 'r').read();
	oldgems = re.findall('"gems":(.+?)',str(task1))[0]

	givegems = task1.replace(oldgems, args2);

	task2 =open(f'C://yourfoldergems69\\{args1}.json', 'w')
	task2.write(givegems)
	task2.close()
	await ctx.send(f"Gems are added to \nPlayer: {args1}\nAmount: {args2}")

@client.command()
async def creator(ctx):
	await ctx.send("Creator: Purge aka TheAmazingPurge")
	await ctx.message.add_reaction("✅")

@client.command()
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.blurple())
    embed.add_field(name="🚧 - : Commands", value="```!status\n!givegem\n!stop\n!start```", inline=False)
    embed.add_field(name="🚧 - : More Commands", value="```!online\n!creator\n!status```", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("✅")

@client.command(alaises=['Cry','Cri','Sad'])
async def cry(ctx):
      embed= discord.Embed(title=f'{ctx.author.name} is crying :sob: , My heart is gonna break!! :broken_heart:  ',
      color=0xdb7bff)
      gifs=['https://media1.tenor.com/images/8f6da405119d24f7f86ff036d02c2fd4/tenor.gif?itemid=5378935',
      'https://media1.tenor.com/images/3b1a145fc182fd2b0cbb29d32e37f43b/tenor.gif?itemid=8572836',
      'https://media1.tenor.com/images/e07ff7159c902150890d84329d253931/tenor.gif?itemid=15021750',
      'https://media1.tenor.com/images/67df1dca3260e0032f40048759a967a5/tenor.gif?itemid=5415917',
      'https://media1.tenor.com/images/213ec50caaf02d27d358363016204d1d/tenor.gif?itemid=4553386',
      'https://media1.tenor.com/images/bdd8e3865332d5ccf2edddd1460e0792/tenor.gif?itemid=16786822',
      'https://media1.tenor.com/images/bc6517ddc10fc60c4dc73c9e3a00eafa/tenor.gif?itemid=13995463]',
      'https://tenor.com/view/oh-no-sad-cry-crying-yui-hirasawa-gif-5415917',
      'https://media.tenor.com/images/224221bb396c782daa0333a23a1c4d51/tenor.gif']
      link= random.choice(gifs)
      embed.set_image(url=f'{link}')
      await ctx.send(embed=embed)

@client.command(alaises=['Smile','Happy','Grin'])
async def smile(ctx):
      embed= discord.Embed(title=f'{ctx.author.name} smiles! :grin:  ',
      color=0xdb7bff)
      gifs=['https://cdn.discordapp.com/attachments/697029214289002539/720796063950176286/image0.gif',
      'https://cdn.discordapp.com/attachments/697029214289002539/720796063950176286/image0.gif',
      'https://images-ext-1.discordapp.net/external/Qj9mj2E1YDcVTespi0Vfig-RiaAc7N0uy88Q0IahBng/https://cdn.weeb.sh/images/rkH84ytPZ.gif?width=400&height=225',
      'https://media.discordapp.net/attachments/697029214289002539/721016708776722574/image0.gif',
      'https://cdn.discordapp.com/attachments/719560200897691728/721351702808363008/image0.gif',
      'http://pa1.narvii.com/6339/ad70e90381a8a5bf9b59657feb86e0bc34108b59_hq.gif?size=450x320']
      link= random.choice(gifs)
      embed.set_image(url=f'{link}')
      await ctx.send(embed=embed)

@client.command(name='logout', aliases=['shutdown'])
@commands.is_owner()
async def botstop(ctx):
    """Turn your bot off"""
    await ctx.send('Goodbye')
    await client.logout()


@client.command()
async def howgay(ctx, member: discord.Member = None):
        member = member or ctx.author
        response=[random.randint(0,100)]
        embed=discord.Embed(title='Gay Rating Device!',
        description=f"\n{member.mention} is {random.choice(response)}% gay!!  :rainbow_flag:",color  = 0xdb7bff)
        await ctx.send(embed=embed)


client.run(token)
