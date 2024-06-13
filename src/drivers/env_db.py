import os
from dotenv import load_dotenv

load_dotenv()

connection_db = os.getenv('MONGODB_CONNECTION_STRING')
print("connection_db ->",connection_db)
