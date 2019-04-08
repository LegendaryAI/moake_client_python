import os
from dotenv import load_dotenv

load_dotenv()

MOAKE_HOST=os.getenv("MOAKE_HOST")
MOAKE_PORT=os.getenv("MOAKE_PORT")
