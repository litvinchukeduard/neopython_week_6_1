from enum import StrEnum, auto
from datetime import datetime
'''
Потрібно написати клас, який буде представляти банківський аккаунт

User(name, surname)

name, surname, amount, currency, unique_code

1) Цей банківський аккаунт має вміти обʼєднуватись з іншими аккаунтами
2) Цей банківський аккаунт має мати операцію поповнення рахунку
3) Додати систему, яка буде зберігати транзакції та дозволятиме їх переглядати
'''

class Currency(StrEnum):
    USD = "United States Dollars"
    EUR = auto()


class BankAccountCurrencyNotSupported(Exception):
    pass


class BankAccount:
    
    def __init__(self, name: str, surname: str, amount: float, currency: str, unique_code: str):
        self.name = name
        self.surname = surname
        self.amount = amount
        self.currency = currency
        self.unique_code = unique_code
        self.transactions = []

    @staticmethod
    def is_add_amount_valid(amount: float) -> bool:
        return amount > 0
    
    def __iter__(self):
        self.iter_index = 0
        return self
    
    def __next__(self):
        if self.iter_index < len(self.transactions):
            transaction = self.transactions[self.iter_index]
            self.iter_index += 1
            return transaction
        else:
            raise StopIteration

    def __add__(self, other):
        if isinstance(other, (int, float)):
            if not BankAccount.is_add_amount_valid(other):
                raise ValueError("Transaction amount can not be negative")
            self.amount += other
            self.transactions.append(f"{datetime.now()} | Added {other} {self.currency} to current account")
            return

        if self.currency != other.currency:
            raise BankAccountCurrencyNotSupported(f"Cannot add bank accounts of type {self.currency} to type {other.currency}")
        if not BankAccount.is_add_amount_valid(other.amount):
                raise ValueError("Transaction amount can not be negative")
        transfer_amount = other.amount
        self.amount += transfer_amount
        other.amount = 0
        self.transactions.append(f"{datetime.now()} | Added {transfer_amount} {self.currency} to current account from account {other.unique_code}")
        return self




# 1)500
# 2)600
# 1) + 2)
# 1) 1100 2) 0

# Two accounts with USD
bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
bank_account_two = BankAccount("John", "Smith", 600, Currency.USD, "000002")
bank_account_one = bank_account_one + bank_account_two
assert bank_account_one.amount == 1100
assert bank_account_two.amount == 0
assert len(bank_account_one.transactions) == 1


# Two accounts with different currencies
bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
bank_account_two = BankAccount("John", "Smith", 600, Currency.EUR, "000002")
try:
    bank_account_one = bank_account_one + bank_account_two
except BankAccountCurrencyNotSupported:
    print("Two accounts with different currencies: passed")
except Exception as e:
    raise AssertionError(f"Code did not raise expected exception, instead was raised {e}")
assert len(bank_account_one.transactions) == 0

bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
bank_account_one + 1000
assert bank_account_one.amount == 1500
assert len(bank_account_one.transactions) == 1


bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
try:
    bank_account_one + (-100)
except ValueError:
    print("Negative number: passed")
except Exception as e:
    raise AssertionError(f"Code did not raise expected exception, instead was raised {e}")
assert len(bank_account_one.transactions) == 0

bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
bank_account_two = BankAccount("John", "Smith", -600, Currency.USD, "000002")
try:
    bank_account_one + bank_account_two
except ValueError:
    print("Negative number account: passed")
except Exception as e:
    raise AssertionError(f"Code did not raise expected exception, instead was raised {e}")
assert len(bank_account_one.transactions) == 0

bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
bank_account_one + 100
bank_account_one + 1 
bank_account_one + 20
for transaction in bank_account_one:
    print(transaction)
