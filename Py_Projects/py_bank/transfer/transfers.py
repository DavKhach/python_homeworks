from datetime import datetime
from typing import List, Optional
from abc import ABC, abstractmethod


class TransactionManager(ABC):
    def __init__(self):
        self.transaction_history: List[str] = []

    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float, to_account: str = None) -> None:
        ...

    def show_transaction_history(self) -> None:
        if not self.transaction_history:
            print("No transaction history.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

class Transaction:
    def __init__(self, from_account: 'Account', to_account: Optional['Account'], amount: float, transaction_type: str):
        from account.accounts import Account

        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def log(self) -> str:
        if self.to_account:
            return f"{self.timestamp} - {self.transaction_type}: ${self.amount} from {self.from_account.get_account_type()} to {self.to_account.get_account_type()}"
        else:
            return f"{self.timestamp} - {self.transaction_type}: ${self.amount} on {self.from_account.get_account_type()}"
