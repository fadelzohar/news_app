from app.config.config import config, ConfigSecure


class CommandIdConfig(config):

    def __init__(self,id):
        config.__init__(self,id)


class CommandConfigSecure(ConfigSecure):

    def __init__(self,id):
        ConfigSecure.__init__(self,id)
