import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'hezzy'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://dash-dash:albert@localhost/pitch'
  
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")
    
class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://dash-dash:albert@localhost/pitch'
    DEBUG = True
   
config_options = {
'development':DevConfig,
'production':ProdConfig


}


   


 





