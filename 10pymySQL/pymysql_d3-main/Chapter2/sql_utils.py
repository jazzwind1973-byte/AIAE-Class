import pymysql
import configparser 
from pymysql.err import IntegrityError
import hashlib


config = configparser.ConfigParser()
config.read('../Chapter1/config.ini')

class SqlManager:
    db_query = "SHOW DATABASES;"

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
                CREATE DATABASE IF NOT EXISTS {database}
            """
            # 執行建立的 SQL 語句
            cursor.execute(sql)
            # 執行查看資料庫
            cursor.execute("SHOW DATABASES;")
            dbs = cursor.fetchall()
        return dbs

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

    # def create_user(name, age, username, password) 建立寫入使用者的 function
    def create_user(self, name, age, username, password):
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    INSERT INTO user (name, age, username, password) 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (name, age, username, hash_password))
        except IntegrityError as e:
            print(f"\033[31m[Error] {username} 已建立\033[0m")
        else:
            self.connection.commit()

    
    def get_user(self, name): # 查詢使用者的 function 
        with self.connection.cursor() as cursor:
            sql = """
                SELECT * FROM user
                WHERE name = %s
            """
            cursor.execute(sql, (name))
            result = cursor.fetchall()

        return result

    def update_password(self, username, password): # 更新使用者的密碼
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        with self.connection.cursor() as cursor:
            sql = """
                UPDATE user SET password = %s
                WHERE username = %s
            """
            cursor.execute(sql, (hash_password, username))

            if cursor.rowcount == 1:
                self.connection.commit()