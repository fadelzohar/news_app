from content_types.config import TypeConfig,TypeConfigSecure,TypeConfigSecureDb
from command.command import CommandInterface
from db.config import connection


class Type(TypeConfigSecureDb,CommandInterface):

    def __init__(self,id):
        TypeConfigSecureDb.__init__(self,id)
        CommandInterface.__init__(self)

    '''
    part of command module
    '''
    def fetch_info(self):
        map = {}
        query = "SELECT * FROM news_types WHERE id={id}".format(id=self.id)
        self._cursor.execute(query)
        fetch = self._cursor.fetchall()
        map.update(
            {
                "record_id": fetch[0][0],
                "type": fetch[0][1]

            }
        )
        return map

    def add_type(self,typeText: str) -> None:

        query = "INSERT INTO news_types(type) VALUES('{type}')".format(type=typeText)
        self._cursor.execute()
        connection.commit()


