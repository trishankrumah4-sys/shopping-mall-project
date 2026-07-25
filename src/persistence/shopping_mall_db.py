import mysql.connector
from mysql.connector import Error

class ShoppingMallDB:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        """Connect to the shopping_mall database"""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=8889,
                user='root',
                password='root',
                database='shopping_mall'
            )
            print("Connected to shopping_mall database")
        except Error as e:
            print(f"Error connecting to database: {e}")
    
    def disconnect(self):
        """Close the database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Disconnected from database")

if __name__ == "__main__":
    db = ShoppingMallDB()
    db.connect()
    db.disconnect()
