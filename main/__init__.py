#ChauhanMahesh/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 7498895
API_HASH = "5204d72f395c291b7257df9631a659ee"
BOT_TOKEN = "5924430427:AAE8Y67N7V7WNqa0u25kqn_QbAMqg3Mg7tE"
BOT_UN = @TESTSAVERRESTRIVBOT
#AUTH_USERS = config("AUTH_USERS", default=None)
#LOG_CHANNEL = config("LOG_CHANNEL", default=None, cast=int)
#ACCESS_CHANNEL = config("ACCESS_CHANNEL", default=None, cast=int)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
