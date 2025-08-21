# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24869695"))
API_HASH = getenv("API_HASH", "5ee98927939d175ca953297fbe309f37")
BOT_TOKEN = getenv("BOT_TOKEN", "8377434516:AAFqN8fOS2o_svX-718B3EKLkHGtOikYTRQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7445620075").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://editingtution99:kLKimOFEX1MN1v0G@cluster0.fxbujjd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002990542830")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003065851438"))
