def count_file_stats(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

            num_lines = len(lines)
            num_words = sum(len(len.split()) for line in lines)
            num_chars = sum(len(len) for line in lines)

        with open(output_file, 'w') as file:
            file.write(f"Lines: {num_lines}")
            file.write(f"Words: {num_words}")
            file.write(f"Characters: {num_chars}")

        print(f"Stats written to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
           

