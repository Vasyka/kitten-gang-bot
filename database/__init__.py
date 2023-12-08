import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import NoResultFound
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from .tables import *

load_dotenv()


class BotDB():
    """Bot Database."""
    def __init__(self):
        """Initialization."""
        self.sqlite_file_name = f"db/bot-database.db"
        self.sqlite_url = f"sqlite+aiosqlite:///{self.sqlite_file_name}"

        self.engine = create_async_engine(self.sqlite_url, echo=True)


    async def init_db_and_tables(self):
        """Initialize the database and the tables."""
        async with self.engine.begin() as session:
            await session.run_sync(SQLModel.metadata.create_all)


    async def add_a_guild(self, discord_guild_id: int, guild_owner_id: int):
        """Add a guild."""
        async with AsyncSession(self.engine) as session:
            guild = await session.exec(select(Guilds).where(Guilds.discord_guild_id == discord_guild_id))
            try:
                guild = guild.one()
                print("Guild already exists.")
                
            except NoResultFound:
                guild = Guilds(discord_guild_id=discord_guild_id, guild_owner_id=guild_owner_id)
                session.add(guild)
                await session.commit()
                await session.refresh(guild)

bot_db = BotDB()