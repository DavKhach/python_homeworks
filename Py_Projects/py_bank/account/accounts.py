from typing import List
from abc import ABC, abstractmethod
from transfer.transfers import TransactionManager


class Account(ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        self.__account_number = account_number
        self.__balance = balance
        self.__account_type = account_type

    @abstractmethod
    def deposit(self, amount: float) -> None:
        ...

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

    @abstractmethod
    def transfer(self, destination: 'Account', amount: float) -> None:
        ...

    @abstractmethod
    def show_balance(self) -> None:
        ...

    @abstractmethod
    def get_account_type(self) -> str:
        ...

    def _get_balance(self) -> float:
        return self.__balance

    def _set_balance(self, balance: float) -> None:
        self.__balance = balance

    def _get_account_type(self) -> str:
        return self.__account_type


class CheckingAccount(Account, TransactionManager):
    def __init__(self, account_number: int, balance: float, overdraft_limit: float = 500):
        Account.__init__(self, account_number, balance, "Checking")
        TransactionManager.__init__(self)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        self._set_balance(self._get_balance() + amount)
        self.log_transaction("Deposit", amount)

    def withdraw(self, amount: float) -> None:
        if self._get_balance() + self.overdraft_limit > amount:
            self._set_balance(self._get_balance() - amount)
            self.log_transaction("Withdrawal", amount)
        else:
            print("Insufficient funds")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if self._get_balance() + self.overdraft_limit > amount:
            self.withdraw(amount)
            destination.deposit(amount)
            self.log_transaction("Transfer", amount, destination._get_account_type())
        else:
            print("Transfer failed")

    def show_balance(self) -> None:
        print(f"Checking Account Balance: {self._get_balance()}")

    def get_account_type(self) -> str:
        return self._get_account_type()

    def log_transaction(self, transaction_type: str, amount: float, to_account: str = None) -> None:
        if to_account:
            self.transaction_history.append(f"{transaction_type}: ${amount} to {to_account}")
        else:
            self.transaction_history.append(f"{transaction_type}: ${amount}")

class SavingsAccount(Account, TransactionManager):
    def __init__(self, account_number: int, balance: float, interest_rate: float):
        Account.__init__(self, account_number, balance, "Savings")
        TransactionManager.__init__(self)
        self.interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        self._set_balance(self._get_balance() + amount)
        self.log_transaction("Deposit", amount)

    def withdraw(self, amount: float) -> None:
        if self._get_balance() > amount:
            self._set_balance(self._get_balance() - amount)
            self.log_transaction("Withdrawal", amount)
        else:
            print("Insufficient funds")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if self._get_balance() > amount:
            self.withdraw(amount)
            destination.deposit(amount)
            self.log_transaction("Transfer", amount, destination._get_account_type())
        else:
            print("Transfer failed")

    def show_balance(self) -> None:
        print(f"Savings Account Balance: {self._get_balance()}")

    def get_account_type(self) -> str:
        return self._get_account_type()

    def log_transaction(self, transaction_type: str, amount: float, to_account: str = None) -> None:
        if to_account:
            self.transaction_history.append(f"{transaction_type}: ${amount} to {to_account}")
        else:
            self.transaction_history.append(f"{transaction_type}: ${amount}")

class JointAccount(Account, TransactionManager):
    def __init__(self, account_number: int, balance: float, joint_owners: List[str]):
        Account.__init__(self, account_number, balance, "Joint")
        TransactionManager.__init__(self)
        self.joint_owners = joint_owners

    def add_owner(self, customer_name: str) -> None:
        self.joint_owners.append(customer_name)
        print(f"{customer_name} added as joint owner.")

    def deposit(self, amount: float) -> None:
        self._set_balance(self._get_balance() + amount)
        self.log_transaction("Deposit", amount)

    def withdraw(self, amount: float) -> None:
        if self._get_balance() > amount:
            self._set_balance(self._get_balance() - amount)
            self.log_transaction("Withdrawal", amount)
        else:
            print("Insufficient funds")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if self._get_balance() > amount:
            self.withdraw(amount)
            destination.deposit(amount)
            self.log_transaction("Transfer", amount, destination._get_account_type())
        else:
            print("Transfer failed: Insufficient funds")

    def show_balance(self) -> None:
        print(f"Joint Account Balance: {self._get_balance()}")

    def get_account_type(self) -> str:
        return self._get_account_type()

    def log_transaction(self, transaction_type: str, amount: float, to_account: str = None) -> None:
        if to_account:
            self.transaction_history.append(f"{transaction_type}: ${amount} to {to_account}")
        else:
            self.transaction_history.append(f"{transaction_type}: ${amount}")
