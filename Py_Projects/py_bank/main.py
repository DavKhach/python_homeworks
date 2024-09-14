from customer.customers import Customer
from account.accounts import CheckingAccount, SavingsAccount, JointAccount


def main():
    checking_account = CheckingAccount(12345, 1000.0)
    savings_account = SavingsAccount(67890, 5000.0, 0.03)
    joint_account = JointAccount(11223, 2000.0, ["Alice", "Bob"])


    customer = Customer("John Doe", "johndoe@example.com")
    customer.add_account(checking_account)
    customer.add_account(savings_account)
    customer.add_account(joint_account)


    checking_account.deposit(500.0)
    checking_account.withdraw(200.0)
    checking_account.transfer(savings_account, 100.0)

    savings_account.deposit(300.0)
    savings_account.withdraw(50.0)

    joint_account.deposit(100.0)
    joint_account.add_owner("Charlie")


    print("\nAccount Balances")
    customer.view_accounts()


    print("\nTransaction History")
    customer.view_transaction_history()

if __name__ == "__main__":
    main()
