import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID, ADMIN_ROLE_ID
from database import get_connection
from typing import Optional


class Profil(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.guilds(GUILD_ID)
    @app_commands.command(
        name="profil",
        description="Wyświetla twój profil operatora"
    )
    async def profil(self, interaction: discord.Interaction):
        if not discord.utils.get(interaction.user.roles):
            return await interaction.response.send_message(
                "❌・Nie masz wymaganych permisji.",
                ephemeral=True
            )

        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute(
            f"SELECT discord_user_id, codename, amount_of_pluses, rank, division FROM operator WHERE discord_user_id = {interaction.user.id}",
        )
        records = cursor.fetchall()

        embed = discord.Embed(
            description=f'## <:goc3:1446906823184482315>・PROFIL OPERATORA\n',
            color=0x002247
        )


        if records:
            for r in records:
                try:
                    member = await interaction.guild.fetch_member(r['discord_user_id'])
                    display_name = member.name
                    pluses = r['amount_of_pluses']
                    division = r['division']
                except discord.NotFound:
                    display_name = "Nie znaleziono użytkownika"

                embed.description = (f"## <:goc3:1446906823184482315>・PROFIL OPERATORA\n* **Operator:** {interaction.user.mention}\n* **Dywizja:** {r['division']}\n* **Liczba plusów:** {r['amount_of_pluses']}")
                embed.set_thumbnail(url=interaction.user.avatar.url)
        else:
            embed.description = "Operator nie został dodany do Bazy"

        conn.commit()
        cursor.close()
        conn.close()

        await interaction.response.send_message(embed=embed, content=f'||{interaction.user.mention}||')


async def setup(bot):
    await bot.add_cog(Profil(bot))