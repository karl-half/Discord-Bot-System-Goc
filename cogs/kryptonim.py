import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID, ADMIN_ROLE_ID, KRYPTONIMY_CHANNEL_ID
from database import get_connection

class KryptonimView(discord.ui.View):
    def __init__(self, kryptonim: str, author_id: int):
        super().__init__(timeout=None)
        self.kryptonim = kryptonim
        self.author_id = author_id

    @discord.ui.button(
        label="Zaakceptuj",
        style=discord.ButtonStyle.primary,
        custom_id="button_1"
    )
    async def accept_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not discord.utils.get(interaction.user.roles, id=ADMIN_ROLE_ID):
            return await interaction.response.send_message(
                "❌・Nie masz wymaganych permisji.",
                ephemeral=True
            )
        
        member = interaction.guild.get_member(self.author_id)
        if not member:
            return await interaction.response.send_message(
                "❌・Nie znaleziono użytkownika.",
                ephemeral=True
            )

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT codename FROM operator WHERE discord_user_id = %s",
            (member.id,)
        )
        result = cursor.fetchone()

        if not result:
            cursor.close()
            conn.close()
            return await interaction.response.send_message(
                f"❌・Użytkownik {member.mention} nie został dodany do bazy danych.",
                ephemeral=True
            )

        cursor.execute(
            "UPDATE operator SET codename = %s WHERE discord_user_id = %s",
            (self.kryptonim, member.id)
        )
        conn.commit()
        cursor.close()
        conn.close()

        await member.edit(nick=f"『 {self.kryptonim} 』")

        embed = interaction.message.embeds[0]
        embed.set_footer(text=f"✅・Zaakceptowano przez {interaction.user.display_name}")

        await interaction.response.edit_message(view=None, embed=embed)

        await interaction.followup.send(
            "✅・Pomyślnie zatwierdzono wniosek o kryptonim.",
            ephemeral=True
        )

    @discord.ui.button(
        label="Odrzuć",
        style=discord.ButtonStyle.danger,
        custom_id="button_2"
    )
    async def deny_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not discord.utils.get(interaction.user.roles, id=ADMIN_ROLE_ID):
            return await interaction.response.send_message(
                "❌・Nie masz wymaganych permisji.",
                ephemeral=True
            )

        member = interaction.guild.get_member(self.author_id)

        if not member:
            return await interaction.response.send_message(
                "❌・Nie znaleziono użytkownika.",
                ephemeral=True
            )

        embed = interaction.message.embeds[0]
        embed.set_footer(text=f"❌・Odrzucono przez {interaction.user.display_name}")

        await interaction.response.edit_message(view=None, embed=embed)

        await interaction.followup.send(
            "❌・Pomyślnie odrzucono wniosek o kryptonim.",
            ephemeral=True
        )



class Kryptonimy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.guilds(GUILD_ID)
    @app_commands.command(
        name="kryptonim",
        description="Wybierz swój kryptonim"
    )
    async def kryptonim(self, interaction: discord.Interaction, kryptonim: app_commands.Range[str, 1, 20]):
        if interaction.channel.id != KRYPTONIMY_CHANNEL_ID:
            return await interaction.response.send_message(
            f'❌ Ta komenda może być użyta tylko w <#{KRYPTONIMY_CHANNEL_ID}>',
            ephemeral=True
        )
        
        embed = discord.Embed(
            description=f'## <:goc3:1446906823184482315>・KRYPTONIM\n* **Kto wybiera:** {interaction.user.display_name}\n* **Kryptonim:** {kryptonim}\n',
            color=0x002247
        )

        embed.set_thumbnail(url=interaction.user.avatar.url)
        # embed.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

        await interaction.response.send_message(embed=embed, view=KryptonimView(kryptonim=kryptonim, author_id=interaction.user.id), content=f'||{interaction.user.mention} <@&1226126217799794698>||')


async def setup(bot):
    await bot.add_cog(Kryptonimy(bot))