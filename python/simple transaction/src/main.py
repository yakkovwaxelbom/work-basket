from customer_manager import CustomerManager
from account_manager import AccountManager


def main():
    db_path = 'database/bank.db'
    cm = CustomerManager(db_path)
    am = AccountManager(db_path)

    customer_id1 = cm.add_customer('Yakov', 'yakov@example.com', '053-361-4312')
    customer_id2 = cm.add_customer('Ben', 'Ben@example.com', '123-456-7890')
    am.create_account(customer_id1, 2000)
    am.create_account(customer_id2, 500)
    print(
        f"Balance before transfer: Customer 1: {am.get_balance(customer_id1)}, Customer 2: {am.get_balance(customer_id2)}")

    am.transfer_funds(customer_id1, customer_id2, 500)

    print(
        f"Balance after transfer: Customer 1: {am.get_balance(customer_id1)}, Customer 2: {am.get_balance(customer_id2)}")


if __name__ == '__main__':
    main()
