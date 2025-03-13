import telegram
from dotenv import load_dotenv
import os


load_dotenv()
tg_token = os.environ['TG_TOKEN']
tg_chat_id = os.environ['TG_CHAT_ID']
bot = telegram.Bot(token=tg_token)

bot.send_document(chat_id=tg_chat_id, document='https://i.ytimg.com/vi/0Ep4Wo0RioA/maxresdefault.jpg')
