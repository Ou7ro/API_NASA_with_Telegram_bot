import telegram
from dotenv import load_dotenv
import os


load_dotenv()
tg_token = os.environ['TG_TOKEN']
bot = telegram.Bot(token=tg_token)

bot.send_message(chat_id='@Nasa_testing_ground', text='Здарова бандиты')
