from config.config import ConfigSecure,config
from db.config import DbConnection


class TypeConfig(config):

    def __init__(self,id):
        config.__init__(self,id)

class TypeConfigSecure(ConfigSecure):

    def __init__(self,id):
        ConfigSecure.__init__(self,id)


class TypeConfigSecureDb(ConfigSecure,DbConnection):

    def __init__(self,id):
        ConfigSecure.__init__(self,id)
        DbConnection.__init__(self)

        