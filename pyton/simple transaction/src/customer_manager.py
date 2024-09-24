from queries import create_customer_query, get_customer_id_query
from transaction_manager import TransactionManager

class CustomerManager:
    def __init__(self, db_path):
        self.tm = TransactionManager(db_path)

    def add_customer(self, name, email, phone):
        self.tm.start_transaction()
        try:
            self.tm.cursor.execute(create_customer_query(), (name, email, phone))
            self.tm.commit_transaction()
            self.tm.cursor.execute(get_customer_id_query(), (email,))
            customer_id = self.tm.cursor.fetchone()[0]
            return customer_id
        except Exception as e:
            self.tm.rollback_transaction()
            print(f"Error adding customer: {e}")
            return None
