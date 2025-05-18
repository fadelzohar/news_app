
from app.config.config import ConfigSecure
from app.writer.config import WriterConfig,WriterConfigSecure,WriterCOnfigSecureDb
from app.command.command import CommandInterface
from app.content.content import content

class WriterOp(WriterCOnfigSecureDb,CommandInterface):

    def __init__(self,id):
        WriterCOnfigSecureDb.__init__(self,id)


    def fetch_info(self):
        map = {}
        query = "SELECT * FROM writer WHERE id={id}".format(id=self.id)
        self._cursor.execute(query)
        fetch = self._cursor.fetchall()
        for writer in fetch:
            content_class = content(writer[0])
            map.update(
                {
                    "id": writer[0],
                    "name": writer[1],
                    "bio": writer[2],
                    "image": "",
                    "contents": content_class.fetch_info()
                }
            )
        return map


    def fetch_contents(self):
        map = []
        query = "SELECT * FROM news writer_id={id}".format(id=self.id)
        self._cursor.execute(query)
        fetch = self._cursor.fetchall()
        for new in fetch:
            map.append(
                {
                    "id": new[0],
                    "date": new[1],
                    "type_id": new[2]
                }
            )
        return map




class CollectionInterface(ConfigSecure):

    def add(self):
        pass

    def remove(self):
        pass

    def edit(self):
        pass





class dashboard(CollectionInterface):

    def __init__(self,CollectionItems: list[WriterOp],StateWriter: WriterConfigSecure):
        self.CollectionItems = CollectionItems
        self.StateWriter = StateWriter



    def add(self):
        self.CollectionItems.append(self.StateWriter)
        return self.CollectionItems

    def remove(self):
        self.CollectionItems.remove(self.StateWriter)
        return self.CollectionItems


    '''
    notify writer operations class
    '''
    def edit(self, UpdateState: WriterConfigSecure):
        self.CollectionItems[self.StateWriter] = UpdateState
        return self.CollectionItems














