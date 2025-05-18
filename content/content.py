from app.config.config import ConfigSecure
from app.content.config import ContentConfig, ContentConfigSecure, ContentConfigSecureDb
from app.command.command import CommandInterface
from app.db.config import connection


class VisitInterface:

    def add_views(self, Content : ContentConfig):
        pass


class ContentVisits(VisitInterface):

    total_views = 0



    def add_views(self, Content: ConfigSecure):
        lens = Content.fetch_views()
        self.total_views += len(lens)
        return self.total_views








class content(ContentConfigSecureDb,CommandInterface):

    def __init__(self,id):
        CommandInterface.__init__(self)
        ContentConfigSecureDb.__init__(self,id)

    '''
    part of command module
    '''

    def fetch_info(self):
        map = {}
        query = "SELECT * FROM new WHERE id={id}".format(id = self.id)
        self._cursor.execute(query)
        fetch = self._cursor.fetchall()
        map.update(
            {
                'record_id': fetch[0][0],
                "writer_id": fetch[0][1],
                "date": fetch[0][2],
                "content": self.fetch_content(),
                "images": self.fetch_images()
            }
        )
        return map


    def fetch_content(self):
        query = "SELECT * FROM news_content WHERE news_id={id}".format(id=self.id)
        self._cursor.execute(query)
        fetch = self._cursor.fetchall
        return fetch[0][2]


    def fetch_images(self):
        map = []
        query = "SELECT * FROM news_images WHERE news_id={id}".format(id=self.id)
        self._cursor.execute(query)
        fetch = self._cursor.fetchall()
        for image in fetch:
            map.append(
                {
                    "record_id": image[0],
                    "image": image[2]
                }
            )
        return map


    def fetch_views(self):
        map = []
        query = "SELECT * FROM user_views WHERE id={id}".format(id=self.id)
        self._cursor.execute(query)
        fetch = self._cursor.fetchall()
        for visit in fetch:
            map.append({
                "record_id": visit[0],
                "cookie": visit[1],
                "is_subscribed": visit[2]
            })
        return map



    '''
    work for views visits class
    '''
    def accept_visits(self, Visits: VisitInterface):
        Visits.add_views(self)



    def update(self,NewUpdate: str) -> None:
        query = "UPDATE news_content WHERE news_id={id}".format(id=self.id)
        self._cursor.execute(query)
        connection.commit()



ob = content(1)
ob.fetch_views()
v = ContentVisits()
ob.accept_visits(v)
print(v.total_views)

'''
class post ->
    class image
    class video
    
class reel ->
    class image
    class video
    
    class factory:
        create post:
        create reel
        
            

'''

