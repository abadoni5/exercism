class BankAccount:
    def __init__(self):
        # Initialize balance to zero and account status to closed
        self._balance = 0
        self._opened = False

    def _raise_error_if_not_open(self):
        # Check if account is not open, raise ValueError if closed
        if not self._opened:
            raise ValueError("account not open")

    def _raise_error_if_amount_less_than_0(self, amount):
        # Check if amount is less than 0, raise ValueError if negative
        if amount < 0:
            raise ValueError("amount must be greater than 0")

    def get_balance(self):
        # Check if account is open, return balance if open
        self._raise_error_if_not_open()
        return self._balance

    def open(self):
        # Check if account is already open, raise ValueError if already open
        if self._opened:
            raise ValueError("account already open")
        # Set account status to open
        self._opened = True

    def deposit(self, amount):
        # Check if account is open and amount is valid
        self._raise_error_if_not_open()
        self._raise_error_if_amount_less_than_0(amount)
        # Add deposit amount to balance
        self._balance += amount

    def withdraw(self, amount):
        # Check if account is open, amount is valid, and balance is sufficient
        self._raise_error_if_not_open()
        self._raise_error_if_amount_less_than_0(amount)
        if amount > self._balance:
            raise ValueError("amount must be less than balance")
        # Deduct withdrawal amount from balance
        self._balance -= amount

    def close(self):
        # Check if account is open, close the account, reset balance to zero
        self._raise_error_if_not_open()
        self._opened = False
        self._balance = 0
