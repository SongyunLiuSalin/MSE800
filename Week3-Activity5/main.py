from database import create_tables, create_connection
from model import Customer, ExchangeRate, Transaction


def menu():
    print("\n==== RMB - NZD Money Exchange System ====")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Add Exchange Rate")
    print("4. Exchange RMB to NZD")
    print("5. View Transactions")
    print("6. Exit")


def view_customers():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer")

    rows = cursor.fetchall()

    conn.close()

    print("\nCustomers:")

    for row in rows:
        print(row)


def view_transactions():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            t.transaction_id,
            c.name,
            t.rmb_amount,
            t.nzd_amount,
            t.transaction_date
        FROM exchange_transaction t
        JOIN customer c
        ON t.customer_id = c.customer_id
    """)

    rows = cursor.fetchall()

    conn.close()

    print("\nTransactions:")

    for row in rows:
        print(row)


def main():

    create_tables()

    while True:

        menu()

        choice = input("Select an option (1-6): ")

        if choice == "1":

            name = input("Enter customer name: ")
            phone = input("Enter phone: ")

            customer = Customer(name, phone)
            customer.save()

        elif choice == "2":

            view_customers()

        elif choice == "3":

            rate = float(input("Enter RMB to NZD rate: "))
            date = input("Enter rate date: ")

            exchange_rate = ExchangeRate(rate, date)
            exchange_rate.save()

        elif choice == "4":

            customer_id = int(input("Enter customer ID: "))
            rate_id = int(input("Enter rate ID: "))
            rmb_amount = float(input("Enter RMB amount: "))
            date = input("Enter transaction date: ")

            transaction = Transaction(
                customer_id,
                rate_id,
                rmb_amount,
                date
            )

            transaction.save()

        elif choice == "5":

            view_transactions()

        elif choice == "6":

            print("Goodbye!")
            break

        else:

            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()