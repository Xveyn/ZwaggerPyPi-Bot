from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

#loead token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#setup bot
intents: Intents = Intents.default()
intents.messages_content = True #NOQA
client: Client = Client(intents=intents)



