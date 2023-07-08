import asyncio
import discord
from discord.ext import commands
from discord.ext import tasks
import GA
import datetime, time
from datetime import timedelta
import secret

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connected: {bot.user.name}')
    send_message_8am.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
   
    if message.channel.id == secret.bot_channel_id:
    
        if message.content.startswith("$얍"):
            channel = message.channel
            await channel.send(message_today_data())

@tasks.loop(seconds=1)
async def send_message_8am():
     now = datetime.datetime.now()
     if now.hour == 18 and now.minute == 55 and now.second == 0:
            await bot.get_guild(secret.bot_server_id).get_channel(secret.bot_channel_id).send(message_yesterday_data())
            time.sleep(1) 


def message_yesterday_data():
      today = datetime.date.today()
      yesterday = today - timedelta(days=1)
      message = ("================\n"
                       f"{yesterday} 기준\n\n"
                f"  당일 DAU {GA.getYesterdayDAU()}\n"
                f"  당월 MAU {GA.getYesterdayMAU()}\n"
                "================\n")
      return message
      
def message_today_data():
      message = ("================\n"
                f"  당일 DAU {GA.getTodayDAU()}\n"
                f"  당월 MAU {GA.getTodayMAU()}\n"
                "================\n")
      return message

bot.run(secret.bot_token)

