import logging
from typing import Dict, List, Optional

import discord
from discord import app_commands


logger = logging.getLogger("discord")

@app_commands.command(name = "hello", description = 'Поздороваться')
async def hello(interaction: discord.Interaction):
	# slash hello command

    guild=interaction.guild
    
    embed = discord.Embed(title = 'Привет!', description="", color=0xff6f00)

    await interaction.response.send_message(embed=embed, ephemeral=False)


@app_commands.command(name = "help", description = 'Посмотреть список команд')
async def help(interaction: discord.Interaction):
    with open('help.txt', 'r') as f:
        info = f.read()
    await interaction.response.send_message(info, ephemeral=True)