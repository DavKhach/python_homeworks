import os

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    return f"Written to {file_name}"

def append_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
    return f"Appended to {file_name}"

def delete_file(file_name):
    os.remove(file_name)
    return f"Deleted {file_name}"


file_operations = {
    'read': read_file,
    'write': write_file,
    'append': append_file,
    'delete': delete_file
}


def file_manager(file_name, operation, content=None):
    if operation not in file_operations:
        raise ValueError("Invalid operaion")

    if operation in ['write', 'append'] and content is None:
        raise ValueError("Content must be provided for write and append operations")

    file_func = file_operations[operation]

    if operation in ['write', 'append']:
        return file_func(file_name, content)
    else:
        return file_func(file_name)

file_name = 'example.txt'

print(file_manager(file_name, 'write', 'Hello World'))
print(file_manager(file_name, 'append', '\nAppended text'))
print(file_manager(file_name, 'read'))
print(file_manager(file_name, 'delete'))
