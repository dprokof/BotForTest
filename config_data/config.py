import os
from dotenv import load_dotenv, find_dotenv

# Проверка наличия переменных
if not find_dotenv():
    exit('Переменные окружения не загружены')
else:
    load_dotenv()

# Базовые переменные
BOT_TOKEN = os.getenv('BOT_TOKEN')
# API_KEY = os.getenv('API_KEY')
DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Вывести справку')
)