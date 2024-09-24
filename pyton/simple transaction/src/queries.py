def create_customer_query():
    return '''
    INSERT INTO Customers (name, email, phone) 
    VALUES (?, ?, ?)
    '''

def create_account_query():
    return '''
    INSERT INTO Accounts (account_id, balance) 
    VALUES (?, ?)
    '''

def get_customer_id_query():
    return '''
    SELECT customer_id 
    FROM Customers 
    WHERE email = ? 
    '''

def update_balance_query():
    return '''
    UPDATE Accounts 
    SET balance = balance + ? 
    WHERE account_id = ?
    '''

def get_balance_query():
    return '''
    SELECT balance 
    FROM Accounts 
    WHERE account_id = ?
    '''

def insert_transaction_query():
    return '''
    INSERT INTO Transactions (account_id, amount, type, status) 
    VALUES (?, ?, ?, ?)
    '''
