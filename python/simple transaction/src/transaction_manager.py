import sqlite3

class TransactionManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.isolation_level = None  # Deadlock
        self.cursor = self.conn.cursor()

    def start_transaction(self):
        self.cursor.execute('BEGIN;')

    def commit_transaction(self):
        self.cursor.execute('COMMIT;')

    def rollback_transaction(self):
        self.cursor.execute('ROLLBACK;')

    def __del__(self):
        self.conn.close()
