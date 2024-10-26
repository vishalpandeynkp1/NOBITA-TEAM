
# All rights reserved.
import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from NOBITAMUSIC import HELPABLE, LOGGER, app, userbot
from NOBITAMUSIC.core.call import NOBITA
from NOBITAMUSIC.plugins import ALL_MODULES
from NOBITAMUSIC.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("NOBITAMUSIC").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("NOBITAMUSIC").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("NOBITAMUSIC.plugins").info("Successfully Imported All Modules ")

    await userbot.start()
    await NOBITA.start()
    await NOBITA.decorators()
    LOGGER("NOBITAMUSIC").info("NOBITAMUSIC STARTED SUCCESSFULLY 🕊️")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("NOBITAMUSIC").info("Stopping NOBITAMUSIC! GoodBye")