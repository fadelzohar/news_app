
from app.config.config import ConfigSecure, ConfigSecureDb,config
from app.writer.config import WriterConfigSecure, WriterCOnfigSecureDb, WriterConfig
from app.content.config import ContentConfigSecure, ContentConfigSecureDb, ContentConfig


class Factory:

    def __init__(self,id):
        pass

    def CreateConfig(self) -> config:

        pass

    def CreateConfigSecure(self) -> ConfigSecure:

        pass

    def CreateConfigSecureDb(self) -> ConfigSecureDb:

        pass



class WriterFactory(Factory):
    def __init__(self,id):
        Factory.__init__(self,id)


    def CreateConfig(self) -> config:
        return WriterConfig(self.id)


    def CreateConfigSecure(self) -> ConfigSecure:
        return WriterConfigSecure(self.id)


    def CreateConfigSecureDb(self) -> ConfigSecureDb:
        return WriterCOnfigSecureDb(self.id)


class ContentFactory(Factory):

    def __init__(self,id):
        Factory.__init__(self,id)


    def CreateConfig(self) -> config:
        return ContentConfig(self.id)

    def CreateConfigSecure(self) -> ConfigSecure:
        return ContentConfigSecure(self.id)

    def CreateConfigSecureDb(self) -> ConfigSecureDb:
        return ContentConfigSecureDb(self.id)





