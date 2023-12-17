import os
import asyncio
import logging
import logging.handlers

from aiohttp import ClientSession
from dotenv import load_dotenv
from typing import List, Optional
from discord.ext import commands

from bot import KittenGangBot



async def main():
    # Logging
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename=f"./logs/discord.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,  #32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    date_format = "%d-%m-%Y %H:%M:%S"
    formatter = logging.Formatter("[{asctime}] [{levelname:<8}] {name}: {message}", date_format, style="{")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Start async session
    async with ClientSession() as web_client:
        async with KittenGangBot(
            commands.when_mentioned,
            web_client=web_client,
            guild_id=os.getenv("GUILD_ID", None),
        ) as client:
            await client.start(os.getenv("DISCORD_TOKEN", ""))

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())