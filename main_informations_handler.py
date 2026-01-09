import discord

async def main_informations(client: discord.Client, information_channel_id: int):
    channel = client.get_channel(information_channel_id)

    def check(_):
        return True

    await channel.purge(limit=None, check=check)


    embed = discord.Embed(
        description='## <:goc3:1446906823184482315>・INFORMACJE OGÓLNE O ORGANIZACJI\n* Na tym kanale zostały zawarte wszystkie najważniejsze informacje o Globalnej Koalicji Okultystycznej. Naciśnij poniżej aby wybrać jedną z opcji i wyświetlić dane informacje.',
        color=0x002247
    )

    # embed.set_image(url="https://i.postimg.cc/g2yT5pMb/informacje-o-organizacji.png")
    embed.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")

    await channel.send(embed=embed, file=discord.File("informacje-o-organizacji.png"), view=MenuView())




class Menu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Jak dołączyć do GKO",
                description="Opis aplikacji o dołączenie do organizacji",
            ),
            
            discord.SelectOption(
                label="Opis Organizacji",
                description="Krótki opis Globalnej Koalicji Okultystycznej",
            ),

            discord.SelectOption(
                label="Hierarchia",
                description="Opisana hierarchia Globalnej Koalicji Okultystycznej",
            ),

            discord.SelectOption(
                label="Pozostałe Role",
                description="Opisana reszta roli na serwerze",
            ),

            discord.SelectOption(
                label="Dywizje",
                description="Opis dywizji i jak do nich dołączyć",
            ),
        ]

        super().__init__(placeholder="Naciśnij aby wybrać opcję", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Jak dołączyć do GKO":
            embedFirst = discord.Embed(
                description='## <:goc3:1446906823184482315>・JAK DOŁĄCZYĆ DO ORGANIZACJI?\n* Aby dołączyć do szeregów Globalnej Koalicji Okultystycznej należy napisać podanie. Znajdziesz takowe na kanale **PLACEHOLDER**. Po naciśnięciu, bot wyśle do Ciebie wiadomość prywatną, tj. pytanie. Po odpowiedzeniu na pierwsze pytanie zostanie Ci wysłane kolejne. Na wszystkie musisz odpowiedzieć. Twoje podanie zostanie sprawdzone przez osoby upoważnione do tego. Może ono zostać rozpatrzone pozytywnie jak i negatywnie. Wyniki są ogłaszane na kanale **PLACEHOLDER**',
                color=0x002247
            )

            embedFirst.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")


            await interaction.response.send_message(embeds=[embedFirst], ephemeral=True)
        elif self.values[0] == "Opis Organizacji":
            embedFirst = discord.Embed(
                description='## <:goc3:1446906823184482315>・CZYM JEST GKO?\n* Globalna Koalicja Okultystyczna znana również jako GKONZ, jest potężną organizacją służącą jako obrońca rasy ludzkiej, nadzorowany przez ONZ. Została założona po II wojnie światowej. Podziela pogląd Fundacji na temat ochrony ludzkości przed tysiącami anomaliami (lub jak nazywają je "parazagrożeniami"), chociaż zamiast je powstrzymywać, zwykle niszczą / zabijają wszystkie napotkane SCP, co czyni ich bardziej kontrowersyjną grupą.',
                color=0x002247
            )

            embedSecond = discord.Embed(
                description='## <:goc3:1446906823184482315>・CZYM ZAJMUJE SIĘ GKO?\n* Głównym zadaniem Globalnej Koalicji Okultystycznej jest ochrona rasy ludzkiej, dlatego w przeciwieństwie do Fundacji SCP, GKO niszczy podmioty SCP a nie je przechowuje.',
                color=0x002247
            )

            embedThird = discord.Embed(
                description='## <:goc3:1446906823184482315>・PIĘCIOKROTNA MISJA GKO\n* Podczas gdy Fundacja SCP ma potrójną misję, Globalna Koalicja Okultystyczna ma pięciokrotną. Deklaracja misji jest następująca i została wymieniona w kolejności od najważniejszej:\n  * Przetrwanie\n  * Ukrywanie\n  * Ochrona\n  * Zniszczenie\n  * Edukacja',
                color=0x002247
            )

            embedThird.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")


            await interaction.response.send_message(embeds=[embedFirst, embedSecond, embedThird], ephemeral=True)
        elif self.values[0] == "Hierarchia":
            embedFirst = discord.Embed(
                description='## <:goc3:1446906823184482315>・HIERARCHIA OGÓLNA JEDNOSTKI\n* **HEAD COUNCIL**\n  * <@&1205607455170633744> - *Dyrektor Globalnej Koalicji Okultystycznej*\n  * <@&1205607455170633743> - *Asystent Dyrektora Globalnej Koalicji Okultystycznej*\n\n* **SUPER HIGH RANK**\n  * <@&1205607455170633739> - *Osoba zarządzająca organizacją*\n  * <@&1205607455170633738> - *Osoba prowadząca oddziały w terenie*\n  * <@&1219677828681957519> - *Osoba prowadząca oddział PHYSICS*\n  * <@&1219677708313690203> - *Osoba prowadząca oddział PSYCHE*\n  * <@&1219677501077585972> - *Osoba prowadząca oddział PTOLEMY*',
                color=0x002247
            )

            embedSecond = discord.Embed(
                description='* **HIGH RANK**\n  * <@&1219729093910724699> - *Ranga za otrzymanie w sumie 100 plusów*\n  * <@&1219729090152501328> - *Ranga za otrzymanie w sumie 90 plusów*\n  * <@&1325107826242097273> - *Ranga za otrzymanie w sumie 80 plusów*\n  * <@&1219682871556575344> - *Ranga za otrzymanie w sumie 70 plusów*\n  * <@&1219682407754764308> - *Ranga za otrzymanie w sumie 60 plusów*\n\n* **MEDIUM RANK**\n  * <@&1205607455149654033> - *Ranga za otrzymanie w sumie 45 plusów*\n  * <@&1205607455149654032> - *Ranga za otrzymanie w sumie 40 plusów*\n  * <@&1205607455149654031> - *Ranga za otrzymanie w sumie 35 plusów*\n  * <@&1325107162824839168> - *Ranga za otrzymanie w sumie 30 plusów*\n  * <@&1205607455149654026> - *Ranga za otrzymanie w sumie 25 plusów*\n\n* **LOW RANK**\n  * <@&1205607455074033712> - *Ranga za otrzymanie w sumie 14 plusów*\n  * <@&1205607455074033711> - *Ranga za otrzymanie w sumie 12 plusów*\n  * <@&1219681520357343286> - *Ranga za otrzymanie w sumie 8 plusów*\n  * <@&1219681606944428153> - *Ranga za otrzymanie w sumie 5 plusów*\n  * <@&1205607455074033710> - *Ranga za otrzymanie w sumie 3 plusów*\n  * <@&1205607455074033709> - *Ranga za otrzymanie w sumie 1 plusa*\n  * <@&1205607455074033708> - *Ranga, którą otrzymuje każdy po zdaniu rekrutacji*',
                color=0x002247
            )

            embedSecond.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")


            await interaction.response.send_message(embeds=[embedFirst, embedSecond], ephemeral=True)
        elif self.values[0] == "Pozostałe Role":
            embedFirst = discord.Embed(
                description='## <:goc3:1446906823184482315>・POZOSTAŁE ROLE\n* **DYWIZJE GKO**\n  * <@&1205607455032086546> - *Rola, którą otrzymują członkowie dywizji PHYSICS*\n  * <@&1205607455074033705> - *Rola, którą otrzymują członkowie dywizji PSYCHE*\n  * <@&1205607455074033706> - *Rola, którą otrzymują członkowie dywizji PTOLEMY*',
                color=0x002247
            )

            embedSecond = discord.Embed(
                description='* **INNE ROLE GKO**\n  * <@&1205607455032086542> - *Osoba odpowiedzialna za wyszkolenie personelu organizacji*\n  * <@&1205607455032086540> - *Osoba nienależąca do naszej organizacji*\n  * <@&1205607455170633741> - *Osoba należąca do administracji Strefy Argon ||`Administrator+`||*',
                color=0x002247
            )

            embedSecond.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")


            await interaction.response.send_message(embeds=[embedFirst, embedSecond], ephemeral=True)
        elif self.values[0] == "Dywizje":
            embedFirst = discord.Embed(
                description='## <:goc3:1446906823184482315>・DYWIZJE GLOBALNEJ KOALICJI OKULTYSTYCZNEJ\n* **DYWIZJA PHYSICS**\n  * Dywizja PHYSICS jest ramieniem operacyjnym GKO, podobnie jak Mobilne Formacje Operacyjne Fundacji. Obserwują, badają, wychwytują i / lub neutralizują anomalie. Dwa główne ramiona tej dywizji to Oddziały Oszacowania (Dochodzenie i Obserwacja) oraz Oddziały Uderzeniowe (Walka i Szturm).\n\n* **DYWIZJA PSYCHE**\n  * Dywizja PSYCHE jest dyplomatycznym ramieniem GKO, które służy jako łącznik ze społecznością paranormalną i stara się utrzymywać pokój z innymi siłami paranormalnymi. Zajmują się bezpośrednim kontaktem z podmiotami SCP oraz niszczeniem ich. Negocjują z nimi, badają je i niszczą.\n\n* **DYWIZJA PTOLEMY**\n  * Dywizja PTOLEMY jest ramieniem pomocniczym GKO. Specjalizują się we włamaniach sieciowych, tzw. Hackerzy. Często potrzebni podczas najazdów w celu skradzenia cennych danych fundacji lub dostania się w niedostępne miejsca. Podczas przebywania w placówce chodzą w strojach bitewnych i pełnym uzbrojeniu.',
                color=0x002247
            )

            embedSecond = discord.Embed(
                description='## <:goc3:1446906823184482315>・JAK DOŁĄCZYĆ DO DYWIZJI?\n* Aby dołączyć do dywizji należy najpierw awansować na stopień <@&1219681606944428153> po czym otworzyć ticket i dać znać przełożonemu jaką dywizję się wybiera.',
                color=0x002247
            )

            embedSecond.set_footer(text='Chronimy ludzkość ponad wszelką cenę, czy im się to podoba czy nie. \nGlobalna Koalicja Okultystyczna', icon_url="https://i.postimg.cc/ZR1qQ6q2/goc6.png")


            await interaction.response.send_message(embeds=[embedFirst, embedSecond], ephemeral=True)



class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Menu())