def process_data(data, /, *, operation="sum"):
    if operation == "sum":
        result = 0
        for num in data:
            result += num
    elif operation == "min":
        result = min(data)
    elif operation == "max":
        result = max(data)
    elif operation == "average":
        result = sum(data) / len(data) if data else 0
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    return result

data = [1,2,3,4,5]
print(process_data(data))
print(process_data(data, operation="max"))
