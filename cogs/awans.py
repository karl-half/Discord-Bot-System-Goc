import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID, ADMIN_ROLE_ID
from database import get_connection


class Awanse(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.guilds(GUILD_ID)
    @app_commands.command(
        name="nadaj-awans",
        description="Nadaj awans danej osobie"
    )
    async def nadaj_awans(self, interaction: discord.Interaction, osoba: discord.Member, powod: str, obecna_rola: discord.Role, nowa_rola: discord.Role, dodatkowe_informacje: str):
        if not discord.utils.get(interaction.user.roles, id=ADMIN_ROLE_ID):
            return await interaction.response.send_message(
                "❌・Nie masz wymaganych permisji.",
                ephemeral=True
            )
        
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT codename FROM operator WHERE discord_user_id = %s",
            (osoba.id,)
        )
        result = cursor.fetchone()

        if not result:
            cursor.close()
            conn.close()
            return await interaction.response.send_message(
                f"❌・Użytkownik {osoba.mention} nie został dodany do bazy danych.",
                ephemeral=True
            )

        cursor.execute(
            "UPDATE operator SET rank = %s WHERE discord_user_id = %s",
            (nowa_rola, osoba.id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        embed = discord.Embed(
            description=f'## <:goc3:1446906823184482315>・NADANO AWANS\n* **Kto nadaje:** {interaction.user.mention}\n* **Komu:** {osoba.mention}\n* **Powód:** {powod}\n* **Poprzednie stanowisko:** {obecna_rola.mention}\n* **Nowe stanowisko:** {nowa_rola.mention}\n* **Dodatkowe informacje:** {dodatkowe_informacje}',
            color=0x002247
        )

        embed.set_thumbnail(url=osoba.avatar.url)

        await interaction.response.send_message(embed=embed, content=f'||{osoba.mention}||')


async def setup(bot):
    await bot.add_cog(Awanse(bot))