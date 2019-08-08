from decouple import config


DEBUG = config("DEBUG", cast=bool)
DATABASE_URI = config("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool)
