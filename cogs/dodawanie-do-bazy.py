import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID, ADMIN_ROLE_ID
from database import get_connection


class DodawanieDoBazy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.guilds(GUILD_ID)
    @app_commands.command(
        name="dodaj-do-bazy",
        description="Dodaj operatora do bazy danych"
    )
    async def dodaj_do_bazy(self, interaction: discord.Interaction, osoba: discord.Member, obecna_rola: discord.Role):
        if not discord.utils.get(interaction.user.roles, id=ADMIN_ROLE_ID):
            return await interaction.response.send_message(
                "❌・Nie masz wymaganych permisji.",
                ephemeral=True
            )

        connect = get_connection()
        cursor = connect.cursor()

        cursor.execute(
            "SELECT discord_user_id FROM operator WHERE discord_user_id = %s",
            (osoba.id,)
        )
        result = cursor.fetchone()

        if result:
            cursor.close()
            connect.close()
            return await interaction.response.send_message(content=f"❌・Użytkownik {osoba.mention} został już dodany do bazy danych.", ephemeral=True)
        else:
            cursor.execute(
                f"INSERT INTO operator(discord_user_id, amount_of_pluses, rank) VALUES (%s, %s, %s)",
                (osoba.id, 0, obecna_rola)
                )

        connect.commit()
        cursor.close()

        await interaction.response.send_message(content=f"✅・Użytkownik {osoba.mention} został pomyślnie dodany do bazy danych.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(DodawanieDoBazy(bot))