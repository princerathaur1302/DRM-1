import os
from os import environ
API_ID = int(environ.get("API_ID", "20214595"))
API_HASH = environ.get("API_HASH", "4763f66ce1a18c2dd491a5048891926c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6775793050"))
CREDIT = "[♛彡 T͙E͙A͙M͙ L͙B͙ 彡♛](https://t.me/contact_262524_bot)"
YT = "[𓊈𒆜Y͎O͎U͎T͎U͎B͎E͎𒆜𓊉](https://youtube.com/@LocalBoyPrince)"
ALL = "[♛A͓̽L͓̽L͓̽ B͓̽A͓̽T͓̽C͓̽H͓̽♛](https://t.me/addlist/Yfez5bB2FiljMzE1)"
AUTH_USER = os.environ.get('AUTH_USERS', '7281824001').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



