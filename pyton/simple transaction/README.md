<<<<<<< HEAD
# work-basket
=======

# Simple Transaction Management System

This is a simple transaction management system implemented in Python using SQLite. The project supports managing customers, accounts, and performing transactions, including money transfers between accounts. It ensures transactional integrity by utilizing SQLite transactions.

## Project Structure

```
simple-transaction/
│
├── src/
│   ├── main.py                # Entry point of the application
│   ├── transaction_manager.py # Manages the database transactions
│   ├── customer_manager.py    # Handles customer-related operations
│   ├── account_manager.py     # Handles account-related operations
│   ├── queries.py             # Contains SQL queries used in the application
│   ├── schema.sql             # Database schema for creating tables
│   └── bank.db                # SQLite database file
│
├── README.md                  # This file
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- SQLite installed on your machine

### Setting Up the Environment

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/simple-transaction.git
   cd simple-transaction
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies:**

   No additional dependencies are required, as the project uses `sqlite3`, which is part of Python's standard library.

4. **Set Up the Database:**

   Run the following command to create the `bank.db` database using the schema defined in `schema.sql`:

   ```bash
   sqlite3 src/bank.db < schema.sql
   ```

5. **Verify Database Setup:**

   You can verify that the tables were created correctly by running:

   ```bash
   sqlite3 src/bank.db
   ```

   Inside the SQLite shell, run:

   ```sql
   .tables
   ```

   You should see the following tables listed: `Customers`, `Accounts`, `Transactions`.

## Running the Application

1. **Run the Application:**

   To start the application, run the following command:

   ```bash
   python src/main.py
   ```

2. **Expected Output:**

   The application will:
   - Create two customers and their accounts.
   - Display the initial balances.
   - Perform a transfer between the accounts.
   - Display the balances after the transfer.

3. **Error Handling:**

   If an error occurs during execution, error messages will be displayed, and the application will roll back transactions as needed.

## Usage

### Adding a Customer

Use the `CustomerManager` class to add a new customer:

```python
from customer_manager import CustomerManager

cm = CustomerManager('bank.db')
customer_id = cm.add_customer('John Doe', 'john@example.com', '123-456-7890')
```

### Creating an Account

Use the `AccountManager` class to create a new account:

```python
from account_manager import AccountManager

am = AccountManager('bank.db')
am.create_account(customer_id, initial_balance=1000)
```

### Transferring Funds

To transfer funds between two accounts:

```python
am.transfer(from_customer_id, to_customer_id, amount=500)
```

### Querying Account Balance

To get the balance of an account:

```python
balance = am.get_balance(customer_id)
print(f"Customer {customer_id} has a balance of {balance}")
```

## Database Schema

The database schema consists of the following tables:

1. **Customers** - Stores customer information (`customer_id`, `name`, `email`, `phone`).
2. **Accounts** - Stores account information (`account_id`, `balance`).
3. **Transactions** - Stores transaction information (`transaction_id`, `account_id`, `amount`, `type`, `status`).

The `schema.sql` file is used to create these tables. It can be executed with the following command:

```bash
sqlite3 src/bank.db < src/schema.sql
```

## Contributing

If you'd like to contribute to this project, feel free to open a pull request or issue on GitHub.

## License

This project is licensed under the MIT License.

## Contact

For any questions, feel free to contact `your-email@example.com`.
>>>>>>> e38ced0 (Initial commit)
