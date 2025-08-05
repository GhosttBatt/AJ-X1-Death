import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26204186"))
API_HASH = getenv("API_HASH","c277a7f93583f68d0fdfdcb68f5fc6c0")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","8209706073:AAH8stU0NeX1IoqTdfAzfVTBQVOzDU5nHDc")

#Get API_KEY from @DeadlineTechOwner or @DeadlineApiBot
API_BASE_URL = getenv("API_BASE_URL", "https://deadlinetech.site")
API_KEY = getenv("API_KEY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ghosttbatt:Ghost2021@ghosttbatt.ocbirts.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002275616383"))

# Get this value from @Harry_RoxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7597135577"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DeadlineTech/music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/aj_bioo")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ARORA_X_MIRACHLE_NETWORK")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGP2BoAny3jHaKC1IiWLUMScYpYEXgPHmkXtz9M0CihxUGngp1cqNFuixfYyNNToLGVe4LOfqQPMEhZ1iAEbLgvRXJ7tR-IEeoGmaxFQ8M96zpxzYxYgPMQyOlJ84tS_eA4EGX8AUNQqow1RVpwU9fBLZiYzQ0Hfd1Lxo3r9hAM3CqHbEtvLvbOmcnI_X0bb8iqIsUcM2bPh8tB9M8lER9mbZz1ApxccwlG_x0Uu5nPqvD5_ze3x9IWQQ3pIngx5yGd0huDRGHLDPtEHzonIz8TCEv96rKfuXdrkif8fj1DeKXMhuxFGX29pWL3WlOCKFqneDtFM1GzYPGTovS0VYiIIjZmIQAAAAHAItULAA")
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


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/pjwlqg.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/ou29gb.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/tny9ug.jpg"
STATS_IMG_URL = "https://files.catbox.moe/k3e3bg.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/nknnw1.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/1xn73k.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/tny9ug.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/fpknxj.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
