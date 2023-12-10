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
		testing_guild_id: Optional[int] = None,
	):
		"""Client initialization."""
		if intents is None:
			intents = discord.Intents.default()
		intents.members = True

		super().__init__(intents=intents)
		self.web_client = web_client
		self.testing_guild_id = testing_guild_id
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

		await self.tree.sync()

		if self.testing_guild_id is not None:
			try:
				testing_guild = discord.Object(self.testing_guild_id)
				testing_guild.owner_id = (await self.fetch_guild(testing_guild.id)).owner_id
				await database.bot_db.add_a_guild(discord_guild_id=testing_guild.id, guild_owner_id=testing_guild.owner_id)
				self.tree.copy_global_to(guild=testing_guild)
				await self.tree.sync(guild=testing_guild)
			except discord.errors.Forbidden:
				print("Bot is not in the testing guild.")
