import pymysql
import configparser 

config = configparser.ConfigParser()
config.read('../Chapter1/config.ini')

class SqlManager:
#def create_db(database)

    def __init__(self, db=None):

        self.connection = pymysql.connect(
            host=config.get('DB', 'host'),
            user=config.get('DB', 'user'),
            password=config.get('DB', 'password'),
            port=config.getint('DB', 'port'),
            cursorclass=pymysql.cursors.DictCursor,
            database=db
    )
    def create_db(self, database):
        with self.connection.cursor() as cursor:
            sql = f"""
                CREATE DATABASE IF NOT EXISTS `{database}`
        """
        # 執行建立的 SQL 語句
            cursor.execute(sql)
        # 執行查看資料庫
            cursor.execute("SHOW DATABASES;")
            dbs = cursor.fetchall()
        return dbs

#def create_user_table(database)

    def create_user_table(self):

        with self.connection.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS user (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    age INT,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL 
                )
            """
            cursor.execute(sql)
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()

        return tables
        def close(self):
            self.connection.Close()

# 查詢使用者的 function


# 建立寫入使用者的 function