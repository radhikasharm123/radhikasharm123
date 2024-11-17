class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:radheybhai@localhost/social_media_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'mysecretkey'
