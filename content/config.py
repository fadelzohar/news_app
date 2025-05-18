from app.config.config import ConfigSecure,config
from app.db.config import DbConnection

class ContentConfig(config):


    def __init__(self,id):
        config.__init__(self,id)


class ContentConfigSecure(ConfigSecure):

    def __init__(self,id):
        ConfigSecure.__init__(self,id)



class ContentConfigSecureDb(ConfigSecure,DbConnection):

    def __init__(self,id):
        ContentConfigSecure.__init__(self,id)
        DbConnection.__init__(self)