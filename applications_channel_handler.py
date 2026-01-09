import discord

async def applications(client: discord.Client, application_channel_id: int, send_to_channel_id: int, public_logs_channel_id: int):
    application_channel_id = client.get_channel(application_channel_id)
    send_to_channel_id = client.get_channel(send_to_channel_id)
    public_logs_channel_id = client.get_channel(public_logs_channel_id)

    def check(_):
        return True

    await application_channel_id.purge(limit=None, check=check)

    embed = discord.Embed(
        description="## <:goc3:1446906823184482315>・REKRUTACJA DO ORGANIZACJI\n* Znajdujesz się na kanale, na którym możesz złożyć rekrutację do Globalnej Koalicji Okultystycznej. Aby rozpocząć rekrutację, wybierz opcję poniżej. Bot wyśle do Ciebie prywatną wiadomość o rozpoczęciu rekrutacji. Po rozpoczęciu będziesz miał 60 minut na odpowiedzenie na wszystkie pytania. W razie problemów prosimy o stworzenie ticketa.",
        color=0x002247
    )

    # embed.set_image(url="https://i.postimg.cc/5yF7yZzr/info-podanie.png")
    embed.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

    await application_channel_id.send(embed=embed, file=discord.File("info-podanie.png"), view=MenuView())


class MenuApps(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Rekrutacja do GKO",
                description="Podanie do Globalnej Koalicji Okultystycznej",
            ),
        ]

        super().__init__(placeholder="Naciśnij aby wybrać opcję", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Rekrutacja do GKO":
            interaction.user.send()

            await interaction.response.send_message(content="Wybrano rekrutację do Globalnej Koalicji Okultystycznej. Sprawdź prywatną wiadomość od bota.", ephemeral=True)


class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuApps())