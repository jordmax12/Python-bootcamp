import datetime
import pytz

class Account(object):
    # static method
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        self.show_balance()
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            print(f"Account {self._name} withdrawing {amount}")
            self._transaction_list.append((Account._current_time(), -amount))
            self._balance -= amount
        else:
            print(f"invalid withdraw ({amount}) for current balance: {self._balance}. ")
        self.show_balance()
    
    def deposit(self, amount):
        if amount > 0:
            print(f"Account {self._name} despositing {amount}")
            self._transaction_list.append((Account._current_time(), amount))
            self._balance += amount
        else:
            print("Deposit amount must be above 0")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self._balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

bank_account = Account("Jordan", 100)
bank_account.withdraw(50)
bank_account.deposit(100)
bank_account.withdraw(50000)
bank_account.show_transactions()

steph = Account("Steph", 800)
steph.deposit(100)
steph.withdraw(200)
steph.show_transactions()