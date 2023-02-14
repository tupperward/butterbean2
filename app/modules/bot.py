import discord, os 
from discord import WelcomeScreen, WelcomeChannel
from discord.ext import commands

# ENV Vars
guildId = os.environ['DISCORD_GUILD_ID','DISCORD_SERVER_ID']
botToken = os.environ['DISCORD_TEST_BOT_TOKEN','DISCORD_BOT_TOKEN']

# Instantiating discord class objects
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
welcomeScreen = WelcomeScreen()

#TODO: Create Class

async def editWelcomeScreen(description: str,channelId: int, channelMessage: str, emoji=None):
  '''Edits as single Welcome Channel at a time asyncronously'''
  await welcomeScreen.edit(
    description=description,
    welcome_channels=[
      WelcomeChannel(channel=channelId, description=channelMessage, emoji=emoji)
    ]
  )

# Run the bot
if __name__=="__main__":
  bot.run(token=botToken)