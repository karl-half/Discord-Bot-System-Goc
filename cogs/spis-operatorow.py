import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID, ADMIN_ROLE_ID
from database import get_connection
from typing import Optional


class SpisOperatorow(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    DIVISIONS = [
        app_commands.Choice(name="PSYCHE", value=1),
        app_commands.Choice(name="PHYSICS", value=2),
        app_commands.Choice(name="PTOLEMY", value=3)
    ]

    @app_commands.guilds(GUILD_ID)
    @app_commands.command(
        name="spis-operatorow",
        description="Wyświetla spis operatorów jednostki"
    )
    @app_commands.choices(dywizja=DIVISIONS)
    async def spis_operatorow(self, interaction: discord.Interaction, dywizja: Optional[int] = None):
        if not discord.utils.get(interaction.user.roles, id=ADMIN_ROLE_ID):
            return await interaction.response.send_message(
                "❌・Nie masz wymaganych permisji.",
                ephemeral=True
            )
        
        conn = get_connection()
        cursor = conn.cursor()

        if dywizja is None:
            cursor.execute(
                "SELECT discord_user_id, codename, amount_of_pluses, rank, division FROM operator",
            )
            records = cursor.fetchall()

            embed = discord.Embed(
                description=f'## <:goc3:1446906823184482315>・SPIS OPERATORÓW JEDNOSTKI\n',
                color=0x002247
            )

            embed.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

            if records:
                for r in records:
                    try:
                        member = await interaction.guild.fetch_member(r['discord_user_id'])
                        display_name = member.name
                    except discord.NotFound:
                        display_name = "Nie znaleziono użytkownika"

                    embed.add_field(
                        name=f"{display_name}",
                        value=f"* ||{member.mention}|| ・ Kryptonim: *{r['codename']}*  ・ Plusy: *{r['amount_of_pluses']}* ・ Dywizja: *{r['division']}*",
                        inline=False
                    )
                    embed.add_field(name="", value="", inline=False)
            else:
                embed.description = "Brak operatorów w bazie."

            conn.commit()
            cursor.close()
            conn.close()


            await interaction.response.send_message(embed=embed, ephemeral=True)

        else:
            match dywizja:
                case 1:
                    cursor.execute(
                        "SELECT discord_user_id, codename, amount_of_pluses, rank, division FROM operator WHERE division = %s",
                        ("PSYCHE")
                    )
                    records = cursor.fetchall()

                    embed = discord.Embed(
                        description=f'## <:goc3:1446906823184482315>・SPIS OPERATORÓW JEDNOSTKI\n### DYWIZJA PSYCHE',
                        color=0x002247
                    )

                    embed.set_footer(
                        text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna',
                        icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

                    if records:
                        for r in records:
                            try:
                                member = await interaction.guild.fetch_member(r['discord_user_id'])
                                display_name = member.name
                            except discord.NotFound:
                                display_name = "Nie znaleziono użytkownika"

                            embed.add_field(
                                name=f"{display_name}",
                                value=f"* ||{member.mention}|| ・ Kryptonim: *{r['codename']}*  ・ Plusy: *{r['amount_of_pluses']}* ・ Dywizja: *{r['division']}*",
                                inline=False
                            )
                            embed.add_field(name="", value="", inline=False)
                    else:
                        embed.add_field(name="Brak operatorów w bazie.", value="")

                    conn.commit()
                    cursor.close()
                    conn.close()

                    await interaction.response.send_message(embed=embed, ephemeral=True)
                case 2:
                    cursor.execute(
                        "SELECT discord_user_id, codename, amount_of_pluses, rank, division FROM operator WHERE division = %s",
                        ("PHYSICS")
                    )
                    records = cursor.fetchall()

                    embed = discord.Embed(
                        description=f'## <:goc3:1446906823184482315>・SPIS OPERATORÓW JEDNOSTKI\n### DYWIZJA PHYSICS',
                        color=0x002247
                    )

                    embed.set_footer(
                        text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna',
                        icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

                    if records:
                        for r in records:
                            try:
                                member = await interaction.guild.fetch_member(r['discord_user_id'])
                                display_name = member.name
                            except discord.NotFound:
                                display_name = "Nie znaleziono użytkownika"

                            embed.add_field(
                                name=f"{display_name}",
                                value=f"* ||{member.mention}|| ・ Kryptonim: *{r['codename']}*  ・ Plusy: *{r['amount_of_pluses']}* ・ Dywizja: *{r['division']}*",
                                inline=False
                            )
                            embed.add_field(name="", value="", inline=False)
                    else:
                        embed.add_field(name="Brak operatorów w bazie.", value="")

                    conn.commit()
                    cursor.close()
                    conn.close()

                    await interaction.response.send_message(embed=embed, ephemeral=True)
                case 3:
                    cursor.execute(
                        "SELECT discord_user_id, codename, amount_of_pluses, rank, division FROM operator WHERE division = %s",
                        ("PTOLEMY")
                    )
                    records = cursor.fetchall()

                    embed = discord.Embed(
                        description=f'## <:goc3:1446906823184482315>・SPIS OPERATORÓW JEDNOSTKI\n### DYWIZJA PTOLEMY',
                        color=0x002247
                    )

                    embed.set_footer(
                        text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna',
                        icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

                    if records:
                        for r in records:
                            try:
                                member = await interaction.guild.fetch_member(r['discord_user_id'])
                                display_name = member.name
                            except discord.NotFound:
                                display_name = "Nie znaleziono użytkownika"

                            embed.add_field(
                                name=f"{display_name}",
                                value=f"* ||{member.mention}|| ・ Kryptonim: *{r['codename']}*  ・ Plusy: *{r['amount_of_pluses']}* ・ Dywizja: *{r['division']}*",
                                inline=False
                            )
                            embed.add_field(name="", value="", inline=False)
                    else:
                        embed.add_field(name="Brak operatorów w bazie.", value="")

                    conn.commit()
                    cursor.close()
                    conn.close()

                    await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(SpisOperatorow(bot))