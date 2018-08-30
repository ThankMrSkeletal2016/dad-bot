# Work with Python 3.6
import discord
import requests
import json

TOKEN = 'TOKKKEN'

client = discord.Client()

prefix = '~'
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith(prefix + 'hello'):
		msg = 'Hello, son'.format(message)
		await client.send_message(message.channel, msg)
	
	
	if message.content.startswith(prefix + 'joke'):
		r = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})
		joke = r.json();
		msg = joke['joke'].format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith(prefix + 'help'):
		msg = 'Commands : hello, joke'.format(message)
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)