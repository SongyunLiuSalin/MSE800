from database import create_connection


class Customer:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO customer (name, phone)
            VALUES (?, ?)
            """,
            (self.name, self.phone)
        )

        conn.commit()
        conn.close()

        print("Customer added successfully.")


class ExchangeRate:

    def __init__(self, rmb_to_nzd, rate_date):
        self.rmb_to_nzd = rmb_to_nzd
        self.rate_date = rate_date

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO exchange_rate (rmb_to_nzd, rate_date)
            VALUES (?, ?)
            """,
            (self.rmb_to_nzd, self.rate_date)
        )

        conn.commit()
        conn.close()

        print("Exchange rate added successfully.")


class Transaction:

    def __init__(
        self,
        customer_id,
        rate_id,
        rmb_amount,
        transaction_date
    ):
        self.customer_id = customer_id
        self.rate_id = rate_id
        self.rmb_amount = rmb_amount
        self.transaction_date = transaction_date

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        # Find the exchange rate
        cursor.execute(
            """
            SELECT rmb_to_nzd
            FROM exchange_rate
            WHERE rate_id = ?
            """,
            (self.rate_id,)
        )

        rate = cursor.fetchone()

        if rate is None:
            print("Exchange rate not found.")
            conn.close()
            return

        # Calculate NZD amount
        nzd_amount = self.rmb_amount * rate[0]

        # Save transaction
        cursor.execute(
            """
            INSERT INTO exchange_transaction
            (
                customer_id,
                rate_id,
                rmb_amount,
                nzd_amount,
                transaction_date
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                self.customer_id,
                self.rate_id,
                self.rmb_amount,
                nzd_amount,
                self.transaction_date
            )
        )

        conn.commit()
        conn.close()

        print("Exchange transaction completed.")
        print(f"RMB: {self.rmb_amount:.2f}")
        print(f"NZD: {nzd_amount:.2f}")