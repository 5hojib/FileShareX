import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
SHORTENER_DOMAIN = os.environ.get('SHORTENER_DOMAIN', '')
SHORTENER_API = os.environ.get('SHORTENER_API', '')
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
