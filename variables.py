import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_CONFIG = {
  "USER_EMAIL": os.getenv("USER_EMAIL"),
  "USER_PASSWORD": os.getenv("USER_PASSWORD")
}
