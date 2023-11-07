import discord
from discord.ext import commands
from discord.ext import tasks
import GA
import totalUser
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
     if now.hour == 8 and now.minute == 0 and now.second == 0:
            await bot.get_guild(secret.bot_server_id).get_channel(secret.bot_channel_id).send(message_yesterday_data())
            time.sleep(1) 


def message_yesterday_data():
      today = datetime.date.today()
      yesterday = today - timedelta(days=1)
      userList = totalUser.getTotalUser()
      message = (
                f"  {yesterday} 기준\n\n"
                f"  어제 DAU: {GA.getYesterdayDAU()}\n"
                f"{GA.getPrevicousMonthMAU()}"
                f"{GA.getCurrentMonthMAU()}"
                f"{GA.get30daysMonthMAU()}\n"
                f"{GA.getYesterdayAverageSessionDuration()}\n"
                f"  누적 가입자수: {userList['totalUser']}\n"
                f"  누적 여성 가입자수: {userList['totalFemaleUser']}\n"
                f"  누적 남성 가입자수: {userList['totalMaleUser']}"
               )
      return message
      
def message_today_data():
      userList = totalUser.getTotalUser()
      message = (
                f"  당일 DAU: {GA.getTodayDAU()}\n"
                f"  당월 누적 MAU: {GA.getTodayMAU()}\n"
                f"{GA.getTodayAverageSessionDuration()}\n"
                f"  누적 가입자수: {userList['totalUser']}\n"
                f"  누적 여성 가입자수: {userList['totalFemaleUser']}\n"
                f"  누적 남성 가입자수: {userList['totalMaleUser']}"
                )
      return message

bot.run(secret.bot_token)