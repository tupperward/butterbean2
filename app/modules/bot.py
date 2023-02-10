import discord, os 
from discord import WelcomeScreen, WelcomeChannel
from discord.ext import commands

# ENV Vars
welcomeChannelId = os.environ['DISCORD_WELCOME_CHANNEL_ID']
rulesChannelId = os.environ['DISCORD_RULES_CHANNEL_ID']
announcementChannelId = os.environ['DISCORD_RULES_CHANNEL_ID']
guildId = os.environ['DISCORD_GUILD_ID','DISCORD_SERVER_ID']
botToken = os.environ['DISCORD_TEST_BOT_TOKEN','DISCORD_BOT_TOKEN']
# Client configuration
intents = discord.Intents.all()

bot = discord.Client(intents=intents)

# TODO: Create a Welcome Screen
# Create Welcome Screen
announcementChannel = bot.get_channel(announcementChannelId)
rulesChannel = bot.get_channel(rulesChannelId)
welcomeChannel = bot.get_channel(welcomeChannelId)
welcomeScreen = WelcomeScreen()

# Run the bot
bot.run(token=botToken)