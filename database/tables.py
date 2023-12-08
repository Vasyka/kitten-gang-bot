from typing import Optional
from sqlmodel import Field, SQLModel


class Guilds(SQLModel, table=True):
    """Guilds table."""
    id: Optional[int] = Field(default=None, primary_key=True)
    logged_in: bool = Field(default=False)
    discord_guild_id: int = Field(unique=True, index=True)
    guild_owner_id: int
