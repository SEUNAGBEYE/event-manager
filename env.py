import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

env = {
  'SECRET_KEY': os.getenv('SECRET_KEY'),
  'ENV': os.getenv('ENV'),
  'EMAIL': os.getenv('EMAIL'),
  'DATABASE': os.getenv('DATABASE'),
  'DATABASE_TEST': os.getenv('DATABASE_TEST'),
  'DATABASE_USER': os.getenv('DATABASE_USER'),
  'DATABASE_PASSWORD': os.getenv('DATABASE_PASSWORD'),
}