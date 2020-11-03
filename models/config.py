"""FlaskのConfigを提供する"""
import os

class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/flask_sample?charset=utf8'.format(**{
    #     'user': os.getenv('DB_USER', 'root'),
    #     'password': os.getenv('DB_PASSWORD', ''),
    #     'host': os.getenv('DB_HOST', 'localhost'),
    # })
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:cteam_pass@db-instance.ciaelricvhfz.us-east-1.rds.amazonaws.com/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig