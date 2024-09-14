from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

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
    def transfer(self, destination: "Account", amount: float) -> None:
        ...

    @abstractmethod
    def show_balance(self) -> None:
        ...

    @abstractmethod
    def get_account_type(self) -> str:
        ...

class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, overdraft_limit: float = 500):
        super().__init__(account_number, balance, "Checking")
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        self.__balance += amount
        print(f"${amount} deposited")

    def withdraw(self, amount: float) -> None:
        if self.__balance - amount >= -self.overdraft_limit:
            self.__balance -= amount
            print(f"${amount} withdrawn.")
        else:
            print("Withdraw denied")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if self.__balance - amount >= -self.overdraft_limit:
            self.withdraw(amount)
            destination.deposit(amount)
            print(f"Transferred ${amount} to account {destination.__account_number}")
        else:
            print("Transfer denied")

    def show_balance(self) -> None:
        print(f"Checking balance: ${self.__balance}")

    def get_account_type(self) -> str:
        return self.__account_type

class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, interest_rate: float):
        super().__init__(account_number, balance, "Savings")
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient budget")

    def transfer(self, destination,amount: float):
        if self.__balance >= amount:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Transfer failed")

    def show_balance(self) -> None:
        print(f"Savings balance: ${self.__balance}")

    def get_account_type(self) -> str:
        return self.__account_type

class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, joint_owners: List[str]):
        super().__init__(account_number, balance, "Joint")
        self.joint_owners = joint_owners

    def add_owner(self, customer_name: str) -> None:
        self.joint_owners.append(customer_name)

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient budget")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if self.__balance >= amount:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Transfer failed")

    def show_balance(self) -> None:
        print(f"Joint balance: ${self.__balance}")

    def get_account_type(self) -> str:
        return self.__account_type


class TransactionManager(ABC):
    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        ...

    def show_transaction_history(self) -> None:
        ...

class Transaction:
    def __init__(self, from_account: "Account", to_account: Optional['Account'], amount: float, transaction_type: str):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def log(self) -> None:
        print(f"Transaction: {self.transaction_type}, Amount: {self.amount}, Timestamp: {self.timestamp}")


