import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID, ADMIN_ROLE_ID
from database import get_connection


class Plusy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.guilds(GUILD_ID)
    @app_commands.command(
        name="daj-plusa",
        description="Daj plusa danej osobie"
    )
    async def daj_plusa(self, interaction: discord.Interaction, osoba: discord.Member, powod: str, ilosc_plusow: int):
        if not discord.utils.get(interaction.user.roles, id=ADMIN_ROLE_ID):
            return await interaction.response.send_message(
                "*❌・Nie masz wymaganych permisji.*",
                ephemeral=True
            )

        connect = get_connection()
        cursor = connect.cursor()

        cursor.execute(
            "SELECT amount_of_pluses FROM operator WHERE discord_user_id = %s",
            (osoba.id,)
        )
        result = cursor.fetchone()

        if result:
            amount_of_pluses = result["amount_of_pluses"]
            new_amount = amount_of_pluses + ilosc_plusow

            cursor.execute(
                "UPDATE operator SET amount_of_pluses = %s WHERE discord_user_id = %s",
                (new_amount, osoba.id)
            )
        else:
            cursor.close()
            connect.close()
            return await interaction.response.send_message(content=f"*❌・Użytkownik {osoba.mention} nie został dodany do bazy danych.*", ephemeral=True)

        connect.commit()
        cursor.close()


        embed = discord.Embed(
            description=f'## <:goc3:1446906823184482315>・NADANO PLUSA\n* **Kto nadaje:** {interaction.user.mention}\n* **Komu:** {osoba.mention}\n* **Powód:** {powod}\n* **Ile plusów nadaje:** {ilosc_plusow}\n* **Który to plus:** {new_amount}',
            color=0x002247
        )

        embed.set_thumbnail(url=osoba.avatar.url)
        # embed.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")


        await interaction.response.send_message(embed=embed, content=f'||{osoba.mention}||')


async def setup(bot):
    await bot.add_cog(Plusy(bot))