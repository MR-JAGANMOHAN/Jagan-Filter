import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'FilesSearch_Robot')
API_ID = int(environ.get('API_ID', '13115322'))
API_HASH = environ.get('API_HASH', 'f28fbd1367ddda2e6f863c3129323743')
BOT_TOKEN = environ.get('BOT_TOKEN', "5851799181:AAGwFmRAM702Fq6F4YIr-ayVRZtOa3Axr7M")

UPDATES_CHANNEL = environ.get("UPDATES_CHANNEL", "nenmemeravtha_1")
HOW_TO_DOWNLOAD = environ.get("HOW_TO_DOWNLOAD", "Telugu_Babai/9")
REQUEST_MOVIES = environ.get("REQUEST_MOVIES", "+xftGUfKVLbkzNzZl")

#Port
PORT = environ.get("PORT", "8080")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/3a8d252ba431d035a2224.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1459910748  5166634607 1795550232 2140794396 1926899055 5336126803 5003515051 1185680029 5010804779 1661667426').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001840167833 -1001979162231 -1001968612719 -1001940538271').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1459910748').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001731898377')
auth_grp = environ.get('AUTH_GROUP', '-1001831982004')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://jagan1857:1857@cluster0.4sgxbb4.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Tgfiles')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001712123362'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+sQwpOdS_cbQzZDE9')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_caption}\n\n<b>⍟──❰ 💝 [TELUGU BABAI](https://telegram.me/TELUGU_BABAI) 💝 ❱──⍟\n\n𝚃𝚑𝚒𝚜 𝙵𝚒𝚕𝚎 𝚆𝚒𝚕𝚕 𝙱𝚎 𝙳𝚎𝚕𝚎𝚝𝚎𝚍 𝚆𝚒𝚝𝚑𝚒𝚗 5 𝙼𝚒𝚗𝚞𝚝𝚎𝚜, 𝚂𝚘 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝙸𝚝 𝚃𝚘 𝚈𝚘𝚞𝚛 𝚂𝚊𝚟𝚎𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜, 𝚃𝚑𝚎𝚗 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍.\n\n⍟──❰ 💝 [TELUGU BABAI](https://telegram.me/TELUGU_BABAI) 💝 ❱──⍟</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "{file_caption}\n\n<b>⍟──❰ 💝 [TELUGU BABAI](https://telegram.me/TELUGU_BABAI) 💝 ❱──⍟\n\n𝚃𝚑𝚒𝚜 𝙵𝚒𝚕𝚎 𝚆𝚒𝚕𝚕 𝙱𝚎 𝙳𝚎𝚕𝚎𝚝𝚎𝚍 𝚆𝚒𝚝𝚑𝚒𝚗 5 𝙼𝚒𝚗𝚞𝚝𝚎𝚜, 𝚂𝚘 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝙸𝚝 𝚃𝚘 𝚈𝚘𝚞𝚛 𝚂𝚊𝚟𝚎𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜, 𝚃𝚑𝚎𝚗 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍.\n\n⍟──❰ 💝 [TELUGU BABAI(https://telegram.me/TELUGU_BABAI) 💝 ❱──⍟</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @TELUGU_BABAI")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001840167833')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'gyanilinks.com')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '195ba82b34f0e8b8bf2c572470bb82e8bd53baaf')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 700))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/Telugu_Babai/9"
   # Custom Caption Under Button #
CAPTION_BUTTON = "❤️‍🔥 Join & Support ❤️‍🔥"
CAPTION_BUTTON_URL = f"https://telegram.me/{UPDATES_CHANNEL}"

