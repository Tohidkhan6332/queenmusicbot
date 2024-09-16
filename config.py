import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "23027390"))

API_HASH = getenv("API_HASH", "70ee33515a12971d9c6a20d59d477c92")

BOT_TOKEN = getenv("BOT_TOKEN", "5812648906:AAH3dlK3nL36sxpN7_8xcpmwlk-Dg1IJpkg")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mohsin:mohsin@cluster0.iauaztt.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", -1001864483206))

OWNER_ID = int(getenv("OWNER_ID", "6987821999"))

BOT_USERNAME = getenv("BOT_USERNAME" , "@Tohidmevati6332_bot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/KRISHtg/queenmusicbot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private



SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+Kus9t8btLPRhYzll")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Kus9t8btLPRhYzll")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦜", "🐝", "🕊️", "🧪", "🕊️", "🔎", "🦋", "🎶", "🪄", "🌡️", "🦜", "🧨"
]

AYUV = [
    "❖ нᴇʏ</b> {0}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n<b>● ʜᴇʏ, ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ꜱᴜᴘᴇʀꜰᴀꜱᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ</b>\n\n<b>● ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ ᴇɴᴊᴏʏ... ɴᴏ ʟᴀɢ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ\n<b>● ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ ᴀɴᴅ ʟᴀɢ ꜰʀᴇᴇ ᴍᴜꜱɪᴄ 🎶\n\n<b>❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠᴄ.</b>\n\nʙᴏᴛ ʀᴇᴘᴏ  ➥ /repo)"
]
    

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []
START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/f6b2e18ecae7ffb6a9c88.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
STATS_IMG_URL = "https://telegra.ph/file/7adee139f0639c400e1b8.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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
