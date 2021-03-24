#This is a complete make and duplicate of ifanps is contoller
# Credit: iFanps
import discord
from discord.ext import commands
from discord import Client
import os, psutil
from datetime import datetime #All the imports

client.remove_command('help')

token = ''
prefix = ''

client = commands.Bot(command_prefix="gt!")

Client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f"Prefix >> [{prefix}]"))

@client.command()
async def status(ctx):
	for proc in psutil.process_iter():
		if 'server' in proc.name():
			await ctx.send("Server is now up!")
		    await ctx.message.add_reaction("✅")
			break;
		else:
			if 'server' not in proc.name():
				await ctx.send("Server is now down.")
			    await ctx.message.add_reaction("✅")

@client.command()
async def online(ctx):
	player = open('online.txt').readlines()
	await ctx.send(f"{listplayer} Accounts created.")
    await ctx.message.add_reaction("✅")

@client.command()
async def player(ctx):
	listplayer = len(os.listdir('players'))
	await ctx.send(f"{listplayer} Account created")
    await ctx.message.add_reaction("✅")

@client.command()
async def start(ctx):
	os.system(r'"server.exe')
	await ctx.send("Your server is up now.")
    await ctx.message.add_reaction("✅")

@client.command()
async def stop(ctx): # iFanp's is stop command.
    gabut = os.system("taskkill /f /im Your enet server.exe")
    if gabut == True:
        await ctx.send("Your server is Down")
        await ctx.message.add_reaction("✅")

@client.command()
async def world(ctx):
	listworld = len(os.listdir('worlds'))
	await ctx.send(f"{listworld} Created for now on.")
    await ctx.message.add_reaction("✅")

@client.command()
async def givegem(ctx, args1, args2):
	task1 = open(f'C://yourfoldergems69\\{args1}.json', 'r').read();
	oldgems = re.findall('"gems":(.+?)',str(task1))[0]

	givegems = task1.replace(oldgems, args2);

	task2 =open(f'C://yourfoldergems69\\{args1}.json', 'w')
	task2.write(givegems)
	task2.close()
	await ctx.send(f"Gems are added to \nPlayer: {args1}\nAmount: {args2}")
    await ctx.message.add_reaction("✅")

@client.command()
async def creator(ctx):
	await ctx.send("Creator: Purge aka TheAmazingPurge")
	await ctx.message.add_reaction("✅")

@client.command()
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.blurple())
    embed.add_field(name="🚧 - :", value="```!status\n!givegem\n!stop\n!start```", inline=False)
    embed.add_field(name="🚧 - :", value="```!online\n!creator\n!status```", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("✅")

client.run(token)
