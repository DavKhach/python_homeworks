def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    data.sort()
    mid = len(data) // 2
    return (data[mid] + data[-mid-1]) / 2


def calculate_mode(data):
    freq = {}
    for num in data:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    if len(modes) == 1:
        return modes[0]
    raise ValueError("No unique mode found")


def calculate_std_dev(data):
    mean = calculate_mean(data)
    return (sum((x - mean) ** 2 for x in data) / (len(data) - 1)) ** 0.5


data_analysis_operations = {
    'mean': calculate_mean,
    'median': calculate_median,
    'mode': calculate_mode,
    'std_dev': calculate_std_dev
}

def analyze_data(data, operation):
    if operation not in data_analysis_operations:
        raise ValueError("Invalid operation")
    return data_analysis_operations[operation](data)



data = [1, 2, 2, 3, 4, 4, 4, 5, 6]


print(analyze_data(data, 'mean'))
print(analyze_data(data, 'median'))
print(analyze_data(data, 'mode'))
print(analyze_data(data, 'std_dev'))
