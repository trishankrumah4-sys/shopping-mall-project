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
    
    # ===== PROMOTION CRUD OPERATIONS =====
    
    def create_promotion(self, promotion_name, description, discount_percent, start_date, end_date):
        """Create a new promotion"""
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO promotion (promotion_name, description, discount_percent, start_date, end_date, is_active)
            VALUES (%s, %s, %s, %s, %s, 1)
            """
            cursor.execute(query, (promotion_name, description, discount_percent, start_date, end_date))
            self.connection.commit()
            print(f"Promotion '{promotion_name}' created successfully")
            cursor.close()
        except Error as e:
            print(f"Error creating promotion: {e}")
    
    def read_all_promotions(self):
        """Read all promotions"""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM promotion"
            cursor.execute(query)
            promotions = cursor.fetchall()
            cursor.close()
            return promotions
        except Error as e:
            print(f"Error reading promotions: {e}")
            return []
    
    def read_promotion_by_id(self, promotion_id):
        """Read a specific promotion by ID"""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM promotion WHERE id = %s"
            cursor.execute(query, (promotion_id,))
            promotion = cursor.fetchone()
            cursor.close()
            return promotion
        except Error as e:
            print(f"Error reading promotion: {e}")
            return None
    
    def update_promotion(self, promotion_id, discount_percent):
        """Update a promotion's discount percent"""
        try:
            cursor = self.connection.cursor()
            query = "UPDATE promotion SET discount_percent = %s WHERE id = %s"
            cursor.execute(query, (discount_percent, promotion_id))
            self.connection.commit()
            print(f"Promotion {promotion_id} updated successfully")
            cursor.close()
        except Error as e:
            print(f"Error updating promotion: {e}")
    
    def delete_promotion(self, promotion_id):
        """Delete a promotion"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM promotion WHERE id = %s"
            cursor.execute(query, (promotion_id,))
            self.connection.commit()
            print(f"Promotion {promotion_id} deleted successfully")
            cursor.close()
        except Error as e:
            print(f"Error deleting promotion: {e}")

if __name__ == "__main__":
    db = ShoppingMallDB()
    db.connect()
    
    print("\n===== STORE CRUD =====")
    stores = db.read_all_stores()
    print(f"Total stores: {len(stores)}")
    
    print("\n===== PROMOTION CRUD =====")
    print("\n--- READ ALL PROMOTIONS ---")
    promotions = db.read_all_promotions()
    print(f"Total promotions: {len(promotions)}")
    for promo in promotions:
        print(promo)
    
    print("\n--- CREATE NEW PROMOTION ---")
    db.create_promotion("Summer Sale", "50% off summer items", 50.00, "2026-06-01", "2026-08-31")
    
    print("\n--- READ ALL PROMOTIONS AGAIN ---")
    promotions = db.read_all_promotions()
    print(f"Total promotions: {len(promotions)}")
    
    print("\n--- UPDATE PROMOTION ---")
    db.update_promotion(1, 75.00)
    
    print("\n--- DELETE PROMOTION ---")
    db.delete_promotion(1)
    
    print("\n--- READ ALL PROMOTIONS FINAL ---")
    promotions = db.read_all_promotions()
    print(f"Total promotions: {len(promotions)}")
    
    db.disconnect()
