import discord.ext
from discord.ext import commands, tasks
from discord.ext.commands import Bot
intents = discord.Intents(messages=True, guilds=True)
intents.messages = True
import random
import asyncio
import time

target_channel_id = [799640609430175797,840380758027141131,853005702715801641,866113380758585375,800507775787859988,853005702715801641]
exterminated= ["30 greeks","1000 greeks","1 greeks","hera","69 greeks","420 greeks","56 greeks greeks","3564 greeks","64 greeks","24 greeks","75 greeks","71 greeks","72 greeks","347 greeks","78 greeks","ares","superweapon","most greek mothers","573257 greeks","greek dignity","6 greeks","540 greeks","57 greeks","54 greeks","17 greeks","75 greeks","75 greeks", "4567 greeks", "2378573 greeks", "kratos", "34 greeks","85 greeks","395 greeks","93 greeks","2817687827168", "276875871857", "956748746"]
#quotes = [":monkima:", "Olivier Levasseur is the best pirate", "Boy, I sure do love Monkey D Luffy and his wacky pirate adventures", "I'm perfectly ok with systemic discrimination, as long as it benefits the economy", "Rainbow capitalism but it's just purple, purple capitalism.", "My natural hair color is green and gold", "My spine is an S for $", "https://media.discordapp.net/attachments/741402122087825561/840396163681222656/image01.gif", "I love capitalism and the system :)", "Work sets me free! :)","I think Will is doing an excellent job running things around here!","Wonderful day, I love our democracy :)", "https://media.tenor.co/videos/8042615bfd52225536ac2bd6aa1faa5e/mp4", "Remember to buy Apple stock!!!", "Corporate social responsibility really works guys!!! I love the enviroment and I know that Will does too!!!! :) :) :)", "Just got done watching the super bowl, those commercials were SOOO hilarious ", "Geee, I love corn syrup :))))", "I fully trust the UN", "Free market, free people. Thats what I always say!!!"]
#target_channel_id = "741454073873825806"
gooddeeds = ['bird','squirrel','fish','local milf','<@434847286259089409>', 'cat','fard','amys ghost', 'ur mum lmao']
bot = commands.Bot(command_prefix=">")
anna = 912772642845634561
josh_id = 700901036986204180
@bot.event
async def on_ready():
	print('ready')
	channel = bot.get_channel(799640609430175797)
	testserverchannel = bot.get_channel(741454073873825806)
	greece = bot.get_channel(945031240862539779)
	#await channel.send("sure")
	#await greece.send(":)")
	await testserverchannel.send("josh is scheming rn")
	#fighting.start()


@tasks.loop(seconds=5)
async def fighting():
   channel = bot.get_channel(random.choice(target_channel_id))
   greece = bot.get_channel(945032333772329000)
   await channel.send(f'{random.choice(exterminated)} have been defeated')
   await greece.send(f'{random.randint(1,1000000)} have been killed')

   #await channel.send("<@619307453867098112> and <@324996062161010690>" + ' has been got')
@bot.event
async def on_message(message):
	member = message.author
	dead = discord.utils.get(message.guild.roles, name = "dead")
	if message.author == bot.user or message.author.bot:
	 	return
	if 'stop' in message.content.lower():
		await message.channel.send('go stop some bitches')
	if 'why' in message.content.lower():
		await message.channel.send('go question some bitches')
	#if 'greek' in message.content.lower():
		#mention = message.author.mention
		#kill = f"{mention} has been killed. Shouldnt have mentioned them."
		#await message.channel.send(kill)
		#await member.add_roles(dead)
	if 'nuke' in message.content.lower():
		await message.channel.send('*sends nukes to ur mums*')
	if 'nuclear' in message.content.lower():
		await message.channel.send('go nuke some bitches')
	if 'retreat' in message.content.lower():
		await message.channel.send('L bozo')
	if ':unsure' in message.content.lower() and message.author.id == 700901036986204180:
		await message.delete()
		await message.channel.send('hmmmm')
	if ':acceptance' in message.content.lower() and message.author.id == 700901036986204180:
		await message.delete()
		await message.channel.send('i like that it kinda sparkly here')
		await message.channel.send('and the giant pit into the void')
		await message.channel.send('ill keep this place safe :)')
		await message.channel.send('im not giving any power back tho')
	if ':ignore' in message.content.lower() and message.author.id == 700901036986204180:
		await message.delete()
		await message.channel.send('*ignores you*')
		await message.channel.send('josh didn program smart responses lmao')
	if ':stare' in message.content.lower() and message.author.id == 700901036986204180:
		mentionUserStr = message.mentions[0].mention
		await message.delete()
		await message.channel.send(f'staring menacingly at {mentionUserStr}')
	if ':attack' in message.content.lower() and message.author.id == 700901036986204180:
		mentionUserStr = message.mentions[0].mention
		await message.delete()
		await message.channel.send(f'im attacking {mentionUserStr}')
	if ':neuter' in message.content.lower() and message.author.id == 700901036986204180:
		await message.delete()
		await message.channel.send('they deaded :)')
	if ':gooddeed' in message.content.lower() and message.author.id == 700901036986204180:
		await message.delete()
		await message.channel.send("helping a " + random.choice(gooddeeds) + " out of a tree")
	if ':mistake' in message.content.lower() and message.author.id == 700901036986204180:
		await message.delete()
		await message.channel.send('whoops')
		time.sleep(2)
		await message.channel.send('i mightve accidentally')
		time.sleep(2)
		await message.channel.send('bonked <@912772642845634561>')
		time.sleep(2)
		await message.channel.send('mightve sucked a hole through your stomach')
		time.sleep(1)
		await message.channel.send('pause ')
		time.sleep(10)
		await message.channel.send('lmao')
#josh speech
	switched = False
	
	if message.author.id == 700901036986204180:
		if 'POWER ON' in message.content:
			switched = True
			print(switched)
		if 'POWER OFF' in message.content:
			switched = False
			print(switched)
		if switched:
			await message.delete()
			await message.channel.send(message.content)
#async def on_message(message):
	#if message.author.id == 741305930695573594:
	#	await message.delete()
	#	await message.channel.send(random.choice(quotes))
#	if message.author.id == 343839193316982785:
#		await message.delete()
	#	await message.channel.send("Hush commie")
	

bot.run('')
