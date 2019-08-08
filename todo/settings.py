from decouple import config


DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URI = config("DATABASE_URI", "postgres+psycopg2://postgres:postgres@localhost:5432/todo_db")

SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATION", cast=bool, default=False)
