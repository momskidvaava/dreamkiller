# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json 
import os

ARQ_API_URL = "https://arq.hamker.in"
ARQ_API_KEY =  "KGTHQB-IKDNAI-XXFCND-VDZFQI-ARQ"

def get_user_list(config, key):
    with open('{}/dreamkiller/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "1480988"   # integer value, dont use ""
    API_HASH = "be76b2fd25b50222b0e1eee141d6a259"
    TOKEN = "5487074903:AAFmMGRsLFPnvKicjZI5giVtivmjrXtr2vY"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5460774651  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "KottayamkunjachanM88"
    SUPPORT_CHAT = 'KanimangalamKovilakam'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'STENZLE_BAN_LOGS' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = -1001792513216  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    EVENT_LOGS = "-1001792513216"  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    LOAD = []
    NO_LOAD = []
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key -
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "5487074903"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    START_IMG = "http://telegra.ph/file/f5226aa2b84b1208cd92e.jpg"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
