import discord
from discord.ext import commands
from config import TOKEN, MAIN_INFORMATION_CHANNEL_ID, GUILD_ID, APPLICATION_CHANNEL_ID, SEND_TO_CHANNEL_ID, PUBLIC_LOGS_CHANNEL_ID
from main_informations_handler import main_informations
from applications_channel_handler import applications


class Client(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.plusy")
        await self.load_extension("cogs.kryptonim")
        await self.load_extension("cogs.wydalenie")
        await self.load_extension("cogs.awans")
        await self.load_extension("cogs.spis-operatorow")
        await self.load_extension("cogs.profil")
        await self.load_extension("cogs.dodawanie-do-bazy")
    
    async def on_ready(self):
        print(f'Zarejestrowano jako {self.user}')

        try:
            synced = await self.tree.sync(guild=GUILD_ID)
            print(f"Zsynchronizowano {len(synced)} komend")
        except Exception as e:
            print(f'Error przy synchronizacji komend: {e}')

        await main_informations(self, MAIN_INFORMATION_CHANNEL_ID)

        await applications(self, APPLICATION_CHANNEL_ID, SEND_TO_CHANNEL_ID, PUBLIC_LOGS_CHANNEL_ID)

        print('Bot pomyślnie wystartowany')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = Client(command_prefix="!", intents=intents)



client.run(TOKEN)