from dotenv import load_dotenv
import os
load_dotenv()

print("DB URI:", os.getenv('DATABASE_URL'))
print("DB URI:", os.getenv('SECRET_KEY'))