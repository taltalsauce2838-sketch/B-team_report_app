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
    def register(self,entry_DB):
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
            INSERT INTO records (
                type, title, body, meta_json, created_at, updated_at
            ) VALUES (
                %(type)s, %(title)s, %(body)s, %(meta_json)s, %(created_at)s, %(updated_at)s
            )
            """
                #実行・確定
                cursor.execute(sql, entry_DB)
                conn.commit()

            
        except pymysql.MySQLError as e:
            print(f"DB処理エラー: {e}")
            conn.rollback()
            exit(1)
        finally:
            conn.close()
    def search(self, sql ,params):
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                #ここで各DBアクセスを実施する
                cursor.execute(sql, params)

                results = cursor.fetchall()

            if len(results) == 0:
                print("データがありません")
                return

            num = 1
            for result in results:
                print(result.get("id")," ",result.get("title")," ",result.get("type"))
                num = num + 1

            return results
                
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
