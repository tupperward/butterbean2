import discord, os 
from discord import WelcomeScreen, WelcomeChannel
from discord.ext import commands
from modules.db import upsertChannelMessage, upsertServerDescription

# ENV Vars
guildId = os.environ['DISCORD_GUILD_ID','DISCORD_SERVER_ID']
botToken = os.environ['DISCORD_TEST_BOT_TOKEN','DISCORD_BOT_TOKEN']

# Instantiating discord class objects
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='/')
welcomeScreen = WelcomeScreen()

@bot.hybrid_command(brief='Edit Welcome Channel', description='Edit a welcome channel message and emoji.')
async def editWelcomeChannel(channelId: int, channelMessage: str, emoji=None):
  '''Edits a single Welcome Channel'''
  await welcomeScreen.edit(
    welcome_channels=[
      WelcomeChannel(channel=channelId, description=channelMessage, emoji=emoji)
    ]
  )
  await upsertChannelMessage(channelId=channelId, channelMessage=channelMessage, emoji=emoji)

# Run the bot
if __name__=="__main__":
  # I think I don't want to actually run this here. I should probably have
  #bot.run(token=botToken)
  print("Hello, World")