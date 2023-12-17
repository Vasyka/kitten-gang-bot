import logging
from typing import Dict, List, Optional

import discord
from discord import app_commands
from player import Player

logger = logging.getLogger("discord")

@app_commands.command(name = "hello", description = 'Поздороваться')
async def hello(interaction: discord.Interaction):
	# hello command
    embed = discord.Embed(title = 'Привет!', description="", color=0xff6f00)

    await interaction.response.send_message(embed=embed, ephemeral=False)


@app_commands.command(name = "help", description = 'Посмотреть список команд')
async def help(interaction: discord.Interaction):
    with open('help.txt', 'r') as f:
        info = f.read()
    await interaction.response.send_message(info, ephemeral=True)

@app_commands.command(name = "profile", description = 'Посмотреть профиль')
async def profile(interaction: discord.Interaction):
    # player profile
    player =  Player(name='Боба',
                     image= 'https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg',
                     player_class = 'Мерзляк',
                     max_hp = 10,
                     hp = 3, defence = 2, heal = 0,
                     exp = 5)
    title = f"{player.player_class} {player.name}"

    embed = discord.Embed(title = title, description = 'кушает пирожочки', color=0x005EB8)
    embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)

    embed.add_field(name="Статы", value=f"""
**Веселье**   {player.hp}/{player.max_hp}
**Нераспределенные очки опыта**   
""", inline=True)

#**Заплатки**   {player.heal}
#**Тепло**   {player.defence}

    embed.add_field(name="Заплатки", value = f"{player.heal}", inline=True)
    embed.add_field(name="Тепло", value=f"{player.defence}", inline=True)


    await interaction.response.send_message(embed=embed)