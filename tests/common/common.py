import os
from dotenv import load_dotenv

load_dotenv()

env = os.environ
BASE_URL = env.get('BASE_URL')
