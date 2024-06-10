from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO magazines (name, category)
            VALUES (?, ?)
        ''', (self.name, self.category))
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
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category cannot be empty")
        self._category = value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM articles WHERE magazine_id = ?
        ''', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors

    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT title FROM articles WHERE magazine_id = ?
        ''', (self.id,))
        titles = cursor.fetchall()
        conn.close()
        return [title[0] for title in titles]

    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT authors.* FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING COUNT(articles.id) > 2
        ''', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors



# class Magazine:
#     def __init__(self, id, name, category):
#         self.id = id
#         self.name = name
#         self.category = category

#     def __repr__(self):
#         return f'<Magazine {self.name}>'
