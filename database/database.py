import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI', '')
db = PostgresqlDatabase(DATABASE_URI)
