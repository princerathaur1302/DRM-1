import os
from os import environ
API_ID = int(environ.get("API_ID", "20214595"))
API_HASH = environ.get("API_HASH", "4763f66ce1a18c2dd491a5048891926c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6775793050"))
CREDIT = "[꧁.💕Ŧ€ΔΜ Łβ💖.꧂](https://t.me/contact_262524_bot)"
AUTH_USER = os.environ.get('AUTH_USERS', '6775793050').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
