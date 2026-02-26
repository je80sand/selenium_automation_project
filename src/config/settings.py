import os
from dotenv import load_dotenv
from pathlib import Path

# Determine which environment to load
ENV = os.getenv("ENV", "dev")

# Build path to correct .env file
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_file = BASE_DIR / f".env.{ENV}"

# Load environment file
load_dotenv(env_file)

# Exposed settings
BASE_URL = os.getenv("BASE_URL")
HEADLESS = os.getenv("HEADLESS") == "1"
CURRENT_ENV = ENV