import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID, ADMIN_ROLE_ID, NIEZIDENTYFIKOWANY_ROLE_ID, NIEZIDENTYFIKOWANY_ZAKLADKA_ROLE_ID


class Wydalanie(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.guilds(GUILD_ID)
    @app_commands.command(
        name="zwolnij",
        description="Zwolnij dan osobę"
    )
    async def zwolnij(self, interaction: discord.Interaction, osoba: discord.Member, powod: str, dodatkowe_informacje: str):
        if not discord.utils.get(interaction.user.roles, id=ADMIN_ROLE_ID):
            return await interaction.response.send_message(
                "*❌・Nie masz wymaganych permisji.*",
                ephemeral=True
            )
        
        embed = discord.Embed(
            description=f'## <:goc3:1446906823184482315>・ZWOLNIONO\n* **Kto wystawia zwolnienie:** {interaction.user.mention}\n* **Kogo zwalnia:** {osoba.mention}\n* **Powód:** {powod}\n* **Dodatkowe informacje:** {dodatkowe_informacje}',
            color=0x002247
        )

        embed.set_thumbnail(url=osoba.avatar.url)
        # embed.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

        await osoba.edit(roles=[])

        newRole1 = interaction.guild.get_role(NIEZIDENTYFIKOWANY_ROLE_ID)
        newRole2 = interaction.guild.get_role(NIEZIDENTYFIKOWANY_ZAKLADKA_ROLE_ID)

        await osoba.add_roles(newRole1, newRole2)

        await osoba.edit(nick=f"")

        await interaction.response.send_message(embed=embed, content=f'||{osoba.mention}||')


async def setup(bot):
    await bot.add_cog(Wydalanie(bot))