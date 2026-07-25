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
    
    # ===== STORE CRUD OPERATIONS =====
    
    def create_store(self, store_name, category, unit_number, floor_level, phone, lease_start_date):
        """Create a new store"""
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO store (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, 1)
            """
            cursor.execute(query, (store_name, category, unit_number, floor_level, phone, lease_start_date))
            self.connection.commit()
            print(f"Store '{store_name}' created successfully")
            cursor.close()
        except Error as e:
            print(f"Error creating store: {e}")
    
    def read_all_stores(self):
        """Read all stores"""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM store"
            cursor.execute(query)
            stores = cursor.fetchall()
            cursor.close()
            return stores
        except Error as e:
            print(f"Error reading stores: {e}")
            return []
    
    def read_store_by_id(self, store_id):
        """Read a specific store by ID"""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM store WHERE id = %s"
            cursor.execute(query, (store_id,))
            store = cursor.fetchone()
            cursor.close()
            return store
        except Error as e:
            print(f"Error reading store: {e}")
            return None
    
    def update_store(self, store_id, phone):
        """Update a store's phone number"""
        try:
            cursor = self.connection.cursor()
            query = "UPDATE store SET phone = %s WHERE id = %s"
            cursor.execute(query, (phone, store_id))
            self.connection.commit()
            print(f"Store {store_id} updated successfully")
            cursor.close()
        except Error as e:
            print(f"Error updating store: {e}")
    
    def delete_store(self, store_id):
        """Delete a store"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM store WHERE id = %s"
            cursor.execute(query, (store_id,))
            self.connection.commit()
            print(f"Store {store_id} deleted successfully")
            cursor.close()
        except Error as e:
            print(f"Error deleting store: {e}")

if __name__ == "__main__":
    db = ShoppingMallDB()
    db.connect()
    
    # Test all CRUD operations
    print("\n===== READ ALL STORES =====")
    stores = db.read_all_stores()
    print(f"Total stores: {len(stores)}")
    for store in stores:
        print(store)
    
    print("\n===== CREATE NEW STORE =====")
    db.create_store("New Mall Store", "Fashion", 205, 2, "555-9999", "2026-01-15")
    
    print("\n===== READ ALL STORES AGAIN =====")
    stores = db.read_all_stores()
    print(f"Total stores: {len(stores)}")
    
    print("\n===== UPDATE STORE =====")
    db.update_store(2, "555-8888")
    
    print("\n===== DELETE STORE =====")
    db.delete_store(2)
    
    print("\n===== READ ALL STORES FINAL =====")
    stores = db.read_all_stores()
    print(f"Total stores: {len(stores)}")
    
    db.disconnect()
