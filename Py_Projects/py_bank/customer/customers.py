from typing import List
from account.accounts import Account
from transfer.transfers import TransactionManager


class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.__accounts: List[Account] = []

    def add_account(self, account: Account) -> None:
        self.__accounts.append(account)

    def view_accounts(self) -> None:
        for account in self.__accounts:
            account.show_balance()

    def view_transaction_history(self) -> None:
        for account in self.__accounts:
            if isinstance(account, TransactionManager):
                print(f"\nTransaction history for {account.get_account_type()} account:")
                account.show_transaction_history()
            else:
                print(f"{account.get_account_type()} account does not support transaction history.")
