import pymysql

class DBAccess:
    def __init__(self):
        self.MYSQL_USERNAME = "root"
        self.MYSQL_PASSWORD = "root"
        self.MYSQL_DATABASE = "standup"

    def get_connection(self):
        try:
            return pymysql.connect(
                host="localhost",
                user=self.MYSQL_USERNAME,
                password=self.MYSQL_PASSWORD,
                database=self.MYSQL_DATABASE,
                cursorclass=pymysql.cursors.DictCursor
        )
        except pymysql.MySQLError as e:
            print(f"データベース接続に失敗しました: {e}")
            exit(1)
    def register(self):
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                #ここで各DBアクセスを実施する
                pass
        except pymysql.MySQLError as e:
            print(f"DB処理エラー: {e}")
            conn.rollback()
            exit(1)
        finally:
            conn.close()
    def search(self):
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                #ここで各DBアクセスを実施する
                pass
        except pymysql.MySQLError as e:
            print(f"DB処理エラー: {e}")
            conn.rollback()
            exit(1)
        finally:
            conn.close()
    def get(self, id):
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM records WHERE id = %s"
                cursor.execute(sql, (id,))
                return cursor.fetchone()
        except pymysql.MySQLError as e:
            print(f"DB処理エラー: {e}")
            conn.rollback()
            exit(1)
        finally:
            conn.close()
