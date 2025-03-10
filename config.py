import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 23578766
API_HASH = "6938361c39c9f76e80ffd4b8b1c18665"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7791635933:AAEqCKste-Xw9aXBNsdBY3VvYbwl94rb1bk"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://toxicdark404:Dark143@cluster0.r9t5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002256730777

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6372485084

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/thanos_pro"
SUPPORT_GROUP = "https://t.me/thanosprosss"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQAnvGwANoh7nwl1rw9DGuBqrC7nOAsMYyf8BJliHvkN-oXSm8xcfc7xhlfyU2cIav4gCAmKlRs6uMdDaPdJ8cvt-ubXEX617AuUV55ZSLLymzccqtyTu7lLOVr3QTiDg1lF585afTRFkj8nl79MPpu8or78guioMi40NXOrsuUjaUpxC_KXPe1xrNMPrLMn4_W_YxfKtRXtZC6F3Kz2ojE46F_bpE-Ta0E3IwnoENiAgYpWwPiJOuPxn9kZY2Sj0soJO_QOul67b4Nqrape5CKrX0VZ9gxjU2uLdyOf2R2UnAR6d6WBxYJXBM7TBzwtG2uoVSnE3tlt3hymsH43LyfOXuInIgAAAAF71GfcAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"

PING_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
STATS_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
STREAM_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/3d8ee0d973764174e0fb2-5f178ded984d13c485.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
