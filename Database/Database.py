import mysql.connector
class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123a45n6",  # Change this to your MySQL password
            database="typing_test_db"
        )
        self.cursor = self.connection.cursor()

    def user_exists(self, username):
        self.cursor.execute("SELECT id FROM users WHERE name = %s", (username,))
        return self.cursor.fetchone()

    def create_user(self, username):
        self.cursor.execute("INSERT INTO users (name) VALUES (%s)", (username,))
        self.connection.commit()
        return self.cursor.lastrowid

    def save_test_result(self, user_id, result):
        self.cursor.execute(
            """
            INSERT INTO test_history (user_id, accuracy, speed, test_date)
            VALUES (%s, %s, %s, NOW())
            """,
            (user_id, result["accuracy"], result["wpm"]),
        )
        self.connection.commit()

    def get_test_history(self, user_id):
        self.cursor.execute(
            """
            SELECT test_date, accuracy, speed FROM test_history
            WHERE user_id = %s ORDER BY test_date DESC
            """,
            (user_id,),
        )
        return self.cursor.fetchall()
