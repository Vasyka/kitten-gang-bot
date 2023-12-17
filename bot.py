from typing import Optional
from aiohttp import ClientSession

import discord
from discord import app_commands

import database
from commands import *

class KittenGangBot(discord.Client):
	def __init__(
		self,
		*args,
		web_client: ClientSession,
		intents: Optional[discord.Intents] = None,
		guild_id: Optional[int] = None,
	):
		"""Client initialization."""
		if intents is None:
			intents = discord.Intents.default()
		intents.members = True

		super().__init__(intents=intents)
		self.web_client = web_client
		self.guild_id = guild_id
		self.tree = app_commands.CommandTree(self)

	async def on_ready(self):
		""" Connection """
		await self.wait_until_ready()
		print(f'Connected! Logged on as {self.user}!')


	async def setup_hook(self) -> None:
		"""Setup"""
		await database.bot_db.init_db_and_tables()

		self.tree.add_command(hello)
		self.tree.add_command(help)
		self.tree.add_command(profile)

		await self.tree.sync()


