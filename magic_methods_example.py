from enum import StrEnum, auto
'''
Потрібно написати клас, який буде представляти банківський аккаунт

User(name, surname)

name, surname, amount, currency, unique_code

1) Цей банківський аккаунт має вміти обʼєднуватись з іншими аккаунтами
2) Цей банківський аккаунт має мати операцію поповнення рахунку
'''

class Currency(StrEnum):
    USD = "united states dollars"
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

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
            return

        if self.currency != other.currency:
            raise BankAccountCurrencyNotSupported(f"Cannot add bank accounts of type {self.currency} to type {other.currency}")
        self.amount += other.amount
        other.amount = 0
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


# Two accounts with different currencies
bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
bank_account_two = BankAccount("John", "Smith", 600, Currency.EUR, "000002")
try:
    bank_account_one = bank_account_one + bank_account_two
except BankAccountCurrencyNotSupported:
    print("passed")
except Exception as e:
    raise AssertionError(f"Code did not raise expected exception, instead was raised {e}")

bank_account_one = BankAccount("Eduard", "Litvinchuk", 500, Currency.USD, "000001")
bank_account_one + 1000
assert bank_account_one.amount == 1500


print(Currency.USD)
