import sqlite3


class DataBaseControl:
    """
    Class for connect database and work with it
    """
    def __init__(self, db_name='chinook.db'):
        self.cursor = self.db_connect(db_name)

    @staticmethod
    def db_connect(database: str):
        """
        Connect to database
        :return:  db cursor to work
        """
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        return cursor

    def db_execute(self, sql_query: str):
        """
        Execute sql commands
        :param sql_query:  string with following sql code
        :return:           list with data from db
        """
        result = self.cursor.execute(sql_query).fetchall()
        return result
