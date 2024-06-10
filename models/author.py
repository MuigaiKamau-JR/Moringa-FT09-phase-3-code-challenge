from database.connection import get_db_connection

class Author:
    def __init__(self, name):
        self.name = name
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO authors (name)
            VALUES (?)
        ''', (self.name,))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        self._name = value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM articles WHERE author_id = ?
        ''', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        ''', (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines





# class Author:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

#     def __repr__(self):
#         return f'<Author {self.name}>'
