import sqlite3
from Config.Config import Config
from pathlib import Path


class DBHandler:
    def __init__(self, dbpath=Config.DATABASE_PATH / Config.BASE_ATTRIBUTE_DB):
        """
        :type dbpath: Path
        """
        self.conn = sqlite3.connect(dbpath.__str__())
        self.cursor = self.conn.cursor()

    def createTable(self, name, **kwargs):
        params = ''
        for key, val in kwargs.items():
            params += f'{key} {val},'

        sql = f"""
      CREATE TABLE {name}
      ({params[:-1]})
      """
        self.cursor.execute(sql)

    def insert(self, table, *args):
        params = ''
        for i in args:
            params += f'{i},'
        return self.cursor.execute(f"""INSERT INTO {table} VALUES ({params[:-1]})""").fetchall()

    def search(self, tablename=None, *args):
        params = ''
        for i in args:
            params += f'{i},'
        return self.cursor.execute(f"""SELECT {params[:-1]} FROM {tablename}""").fetchall()

    def createFromModel(self, model):
        pass


if __name__ == '__main__':
    te = DBHandler()
    # te.createTable('BaseAttribute',a='int',b='int')
    te.insert('BaseAttribute', 2, 3)
    print(te.search('BaseAttribute', '*'))
