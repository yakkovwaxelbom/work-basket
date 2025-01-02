# account_manager.py

from queries import create_account_query, update_balance_query, get_balance_query, insert_transaction_query
from transaction_manager import TransactionManager


class AccountManager:
    def __init__(self, db_path):
        self.tm = TransactionManager(db_path)

    def create_account(self, customer_id, initial_balance):
        self.tm.start_transaction()
        try:
            self.tm.cursor.execute(create_account_query(), (customer_id, initial_balance))
            self.tm.commit_transaction()
        except Exception as e:
            self.tm.rollback_transaction()
            print(f"Error creating account: {e}")

    def update_balance(self, account_id, amount):
        self.tm.cursor.execute(update_balance_query(), (amount, account_id))
        self.tm.commit_transaction()
        self.tm.cursor.execute(insert_transaction_query(), (account_id, amount, 'Update', 'Completed'))
        self.tm.commit_transaction()

    def get_balance(self, account_id):
        try:
            self.tm.cursor.execute(get_balance_query(), (account_id,))
            result = self.tm.cursor.fetchone()
            if result is None:
                print(f"Error: Account with ID {account_id}. not found")
                return None
            return result[0]
        except Exception as e:
            print(f"Error getting the balance for an account {account_id}: {e}")
            return None

    def transfer_funds(self, from_account_id, to_account_id, amount):
        self.tm.start_transaction()
        try:
            self.tm.cursor.execute(get_balance_query(), (from_account_id,))
            from_balance = self.tm.cursor.fetchone()[0]

            if from_balance < amount:
                raise ValueError("There is not enough balance in the transferring account")

            self.tm.cursor.execute(update_balance_query(), (-amount, from_account_id))
            self.tm.cursor.execute(update_balance_query(), (amount, to_account_id))

            self.tm.cursor.execute(insert_transaction_query(), (from_account_id, -amount, 'Transfer Out', 'Completed'))
            self.tm.cursor.execute(insert_transaction_query(), (to_account_id, amount, 'Transfer In', 'Completed'))

            self.tm.commit_transaction()
            print(
                f"Transfer of {amount}& from account {from_account_id} to account {to_account_id} successfully executed.")

        except Exception as e:
            self.tm.rollback_transaction()
            print(f"Transfer error: {e}")
