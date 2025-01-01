import mysql.connector
# Connect to MySQL server (without selecting a database)
def connect_to_server():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123a45n6"  # Change this to your MySQL password
    )

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Change this to your MySQL password
        database="typing_test_db"
    )

# Function to initialize database and tables
def initialize_database():
    # Create database if not exists
    server_connection = connect_to_server()
    cursor = server_connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS typing_test_db")
    server_connection.close()

    # Connect to the database and create tables
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            accuracy FLOAT NOT NULL,
            speed FLOAT NOT NULL,
            test_date DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    connection.commit()
    connection.close()