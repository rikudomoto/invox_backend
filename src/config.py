import os


class DevelopmentConfig:

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
            **{
                "user": os.getenv("DB_USER", "root"),
                "password": os.getenv("DB_PASSWORD", "password"),
                "host": os.getenv("DB_HOST", "db"),
                "database": os.getenv("DB_DATABASE", "invox_db"),
            }
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
