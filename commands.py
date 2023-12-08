import logging
from typing import Dict, List, Optional

import discord
from discord import app_commands


logger = logging.getLogger("discord")

@app_commands.command(name = "hello", description = 'Поздороваться')
async def hello(interaction: discord.Interaction) -> None:
	# slash hello command

    guild=interaction.guild
    #green_candy = discord.utils.get(guild.emojis, name='candy1')
    
    embed = discord.Embed(title = 'Привет котенок! :smile_cat:', description="", color=0xff6f00)
    embed.set_footer(text="Хехе")

    await interaction.response.send_message(embed=embed, ephemeral=True)