import json

def filter_json(input_file, output_file, attribute, value):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)

        try:
            iter(data)
        except TypeError:
            print(f"Error: The data in {input_file} is not iterable")
            return

        filtered_data = []
        for entry in data:
            try:
                if entry[attribute] == value:
                    filtered_data.append(entry)
            except (KeyError, TypeError, AttributeError):
                print(f"Skipping non-dictionary item: {entry}")

        with open(output_file, 'w') as file:
            json.dump(filtered_data, file, indent=4)

        print(f"Filtered data written to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {input_file}")


filter_json("data.json", "filter_data.json", 'status', 'active')
