from decouple import config


DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URI = config("DATABASE_URI", "sqlite:///app.db")

SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATION",
        cast=bool, default=False)
