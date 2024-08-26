def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file_path = "example.txt"
for line in read_file_lines(file_path):
    print(line)
