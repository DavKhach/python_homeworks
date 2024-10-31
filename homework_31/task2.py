import multiprocessing
import csv
import os


def process_file(file_path):
    total_amount = 0
    transaction_count = 0

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_amount += float(row['Amount'])
            transaction_count += 1

    return total_amount, transaction_count


def check_file_path(file_name):
    directory = "C:\\code\\homework_31"
    file_path = os.path.join(directory, file_name)
    return process_file(file_path)

def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    pool = multiprocessing.Pool()
    results = pool.map(check_file_path, csv_files)

    total_amount = sum(amount for amount, _ in results)
    total_transactions = sum(transactions for _, transactions in results)

    print(f"Total Transactions: {total_transactions}")
    print(f"Total Amount: ${total_amount:.2f}")

if __name__ == "__main__":
    main()

