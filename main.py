import discord
import os
import asyncio
from discord.ext import commands
from colorama import Fore, Style, init
from dotenv import load_dotenv  # <--- NEW IMPORT

# 1. Load the .env file immediately
load_dotenv()

# Initialize colors
init(autoreset=True)

# Configuration
INTENTS = discord.Intents.all()
PREFIX = "!"

class SentinelX(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX, intents=INTENTS, help_command=None)

    async def setup_hook(self):
        # Load all security modules from the /cogs directory
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f"[{Fore.GREEN}MODULE{Style.RESET_ALL}] Loaded: {filename}")

    async def on_ready(self):
        # We use r""" for raw strings to fix the SyntaxWarning about backslashes
        print(Fore.RED + r"""
   _____  ______  _   _  _______  _____  _   _  ______  _       __   __
  / ____||  ____|| \ | ||__   __||_   _|| \ | ||  ____|| |      \ \ / /
 | (___  | |__   |  \| |   | |     | |  |  \| || |__   | |       \ V / 
  \___ \ |  __|  | . ` |   | |     | |  | . ` ||  __|  | |        > <  
  ____) || |____ | |\  |   | |    _| |_ | |\  || |____ | |____   / . \ 
 |_____/ |______||_| \_|   |_|   |_____||_| \_||______||______| /_/ \_\
              https://github.com/devnand-47
              ⚠️ Disclaimer
This tool is for defensive purposes only. It is designed to protect communities. The developer (Dev_Nand) is not responsible for misuse of the source code.
        """ + Style.RESET_ALL)
        print(f"[{Fore.CYAN}SYSTEM{Style.RESET_ALL}] SentinelX is Online.")
        print(f"[{Fore.CYAN}STATUS{Style.RESET_ALL}] Monitoring {len(self.guilds)} servers.")
        await self.change_presence(activity=discord.Game(name="Securing Systems | !help"))

if __name__ == "__main__":
    bot = SentinelX()
    
    try:
        # Now this will actually work because load_dotenv() ran first
        token = os.getenv("DISCORD_TOKEN")
        if token:
            bot.run(token)
        else:
            print(f"[{Fore.YELLOW}WARNING{Style.RESET_ALL}] No token found. Please check your .env file.")
    except Exception as e:

        print(e)
