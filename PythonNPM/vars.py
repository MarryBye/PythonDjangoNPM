from os import getenv
from dotenv import load_dotenv

load_dotenv()

DJANGO_KEY = getenv('DJANGO_KEY')
SETTINGS_FILE = getenv('SETTINGS_FILE')