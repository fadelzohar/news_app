from db.config import DbConnection,connection
from config.config import ConfigSecure,config


class WriterConfig(config):
    def __init__(self,id):
        config.__init__(self,id)


class WriterConfigSecure(ConfigSecure):
    def __init__(self,id):

        ConfigSecure.__init__(self,id)

class WriterCOnfigSecureDb(ConfigSecure,DbConnection):

    def __init__(self,id):

        ConfigSecure.__init__(self,id)
        DbConnection.__init__(self)