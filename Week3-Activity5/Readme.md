# RMB - NZD Money Exchange System

This project is a simple money exchange system developed using Python and SQLite.

The system supports RMB to NZD currency exchange.

## Database Tables

The database has 3 tables.

### 1. Customer

Stores customer information.

- customer_id
- name
- phone

This table is needed to store information about customers.

### 2. Exchange Rate

Stores the RMB to NZD exchange rate.

- rate_id
- rmb_to_nzd
- rate_date

This table is needed because exchange rates can change.

### 3. Exchange Transaction

Stores currency exchange transactions.

- transaction_id
- customer_id
- rate_id
- rmb_amount
- nzd_amount
- transaction_date

This table is needed to record each exchange transaction.

## OOP

The project uses Python OOP with three entities:

- Customer
- ExchangeRate
- Transaction
