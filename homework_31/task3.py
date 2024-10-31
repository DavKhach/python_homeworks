import asyncio
import json
import aiofiles


async def read_json_file(file_path):
    async with aiofiles.open(file_path, 'r') as file:
        data = await file.read()
        return json.loads(data)

async def process_user_data(file_path):
    user_data = await read_json_file(file_path)
    user_names = [user['name'] for user in user_data]
    total_purchase_amount = {user['name']: sum(purchase['amount'] for purchase in user['purchases']) for user in user_data}
    return user_names, total_purchase_amount

async def main():
    file_paths = ['user_data.json']
    tasks = [process_user_data(file_path) for file_path in file_paths]
    results = await asyncio.gather(*tasks)

    for user_names, total_purchase_amount in results:
        print("User Names:", user_names)
        print("Total Purchase Amounts:")
        for name, amount in total_purchase_amount.items():
            print(f"{name}: {amount}")

if __name__ == "__main__":
    asyncio.run(main())

