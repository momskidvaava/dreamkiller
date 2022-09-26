import json
import os


def get_user_list(config, key):
    with open("{}/dreamkiller/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    
    BOT_ID = "5767549463"
    AI_API_KEY = ""
    API_ID = "1480988"
    API_HASH = "be76b2fd25b50222b0e1eee141d6a259"
    TOKEN = "5605728947:AAHGZRsBITZF6LY8L4_08pGwvdcMkKpXrCE"
    OWNER_ID = "5616310867"
    OWNER_USERNAME = "KRISHNA_THULSI"
    SUPPORT_CHAT = "KanimangalamKovilakam"
    JOIN_LOGGER = (-1001792513216)
    EVENT_LOGS = (-1001792513216)
    DATABASE_URL = "postgres://mazbpceceqsass:5b1678e5d3f2353460a71c26074f76fb91dc946a184477cc127241c09845ce9a@ec2-54-155-112-143.eu-west-1.compute.amazonaws.com:5432/d3oo4isc6qjsvv"
    SQLALCHEMY_DATABASE_URI = "sqldbtype://username:pw@hostname:port/db_name"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = "https://t.me/KRISHNA_THULSI"
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    SPAMWATCH_API = "CfJJPMqNfU~IIrQDSf~RJCBFcOvbB0QkOPPCqfBG_ScN1rJ_H7ZudCjXFvswy2S~"  # go to support.spamwat.ch to get key -
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "http://tele.gra.ph/file/4cbb01809bc01b6ab68d4.jpg"  
    TEMP_DOWNLOAD_DIRECTORY = "./  
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
