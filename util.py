import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime, timedelta, timezone
import pytz


load_dotenv()

groq_client = Groq(
    api_key=os.environ.get('GROQ_API_KEY'),  # Masukan Api Key Groq ke Secrets
)


def get_current_time():
    current_time = datetime.now(timezone.utc)
    adjusted_time = current_time + timedelta(hours=7)
    return adjusted_time.strftime('%H:%M')
