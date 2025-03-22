import logging, logging.config
import os
from telegram import Bot

# Configure logging
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Get the bot token from the environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def log_bot_username():
    if TOKEN is None:
        logger.error("Bot token not found. Please set the TELEGRAM_BOT_TOKEN environment variable.")
        return
    
    # Initialize the bot
    bot = Bot(token=TOKEN)
    
    # Fetch the bot's information
    bot_info = bot.get_me()
    
    # Log the bot's username
    logger.info(f"Deployment connected to @{bot_info.username}")

# Call the function to log the bot's username
log_bot_username()
