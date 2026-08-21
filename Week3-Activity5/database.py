import sqlite3


def create_connection():
    conn = sqlite3.connect("money_exchange.db")
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Customer table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    # Exchange Rate table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rate (
            rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
            rmb_to_nzd REAL NOT NULL,
            rate_date TEXT NOT NULL
        )
    """)

    # Exchange Transaction table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_transaction (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            rate_id INTEGER NOT NULL,
            rmb_amount REAL NOT NULL,
            nzd_amount REAL NOT NULL,
            transaction_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
            FOREIGN KEY (rate_id) REFERENCES exchange_rate(rate_id)
        )
    """)

    conn.commit()
    conn.close()