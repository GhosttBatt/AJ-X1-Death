import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26204186"))
API_HASH = getenv("API_HASH","c277a7f93583f68d0fdfdcb68f5fc6c0")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","8379997770:AAEZL6q-cpX5NNZVuRob2s9M0xrZtXnYUA0")

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

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/yuvabio")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/yuvaupdatesabout")

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
STRING1 = getenv("STRING_SESSION", "BQE_0DUAf--CZbwj_ewSGiOR1cZ4ewZFFV3BpTXm5p9xFMDscKDoqIVxieJuy8eAAklsOkU_hhLh8X6r6i0XginTna7pohYa3dmkFXhqMPp3tKUtxbkW7qK1Z4W2Y3YhYiHbPmECidbQFPI82gFIyFvAiwb8aS33M-rX8etKPImSASPTzvbZsEo8j0xdsKdWNfHF2-y6SjwYysOOGrEgomeGDRXXY0We4YS4AH9SbUKFDL_sjveg5wKMeAXUu2NCGsl7xWAcL6N-inUpiMmHnJTDDw_SkQZdM5UNskBRo9bTKXahfQrP2quBxmR1WtWPjSnVcgSYCsWdVb5wtHpLJD3lPUvTSgAAAAH5I7cOAA")
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
    "START_IMG_URL", "https://files.catbox.moe/qnx4wo.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/qnx4wo.jpg"
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
