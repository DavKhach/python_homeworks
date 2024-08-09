def retry(num_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(num_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == num_retries - 1:
                        raise
                    print("Retrying...")

        return wrapper
    return decorator


@retry(num_retries=5)
def read_file(filename):
    print(f"Reading file {filename}")
    with open(filename, 'r') as file:
        return file.read()


try:
    content = read_file("non_existent_file.txt")
    print(content)
except Exception as e:
    print(f"Failed to read file after multiple attempts: {e}")
