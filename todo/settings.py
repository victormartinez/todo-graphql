from decouple import config


DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URI = config("DATABASE_URI", "sqlite:///db.sqlite3")

SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATION",
        cast=bool, default=False)
