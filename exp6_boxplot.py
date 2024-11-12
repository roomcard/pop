import csv

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        rows = [float(row[0]) for row in reader]
    return rows

def five_number_summary(data):
    data = sorted(data)
    n = len(data)
    
    min_val = data[0]
    max_val = data[-1]
    
    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]
    
    lower_half_array = data[:n // 2]
    upper_half_array = data[n // 2 + 1:] if n % 2 != 0 else data[n // 2:]

    if len(lower_half_array) % 2 == 0:
        q1 = (lower_half_array[len(lower_half_array) // 2 - 1] + lower_half_array[len(lower_half_array) // 2]) / 2
    else:
        q1 = lower_half_array[len(lower_half_array) // 2]

    if len(upper_half_array) % 2 == 0:
        q3 = (upper_half_array[len(upper_half_array) // 2 - 1] + upper_half_array[len(upper_half_array) // 2]) / 2
    else:
        q3 = upper_half_array[len(upper_half_array) // 2]

    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    if(lower_bound<0):lower_bound=0
    upper_bound = q3 + 1.5 * iqr

    actual_min = min_val
    actual_max = max_val
    outliers = []

    for val in data:
        if val >= lower_bound and val <= upper_bound:
            if val < actual_max:
                actual_max = val
            if val > actual_min:
                actual_min = val
        else:
            outliers.append(val)

    return {
        "Min": min_val,
        "Q1": q1,
        "Median": median,
        "Q3": q3,
        "Max": max_val,
        "Upper Bound": upper_bound,
        "Lower Bound": lower_bound,
        "Interquartile Range": iqr,
        "Outliers": outliers
    }

def write_summary_to_csv(output_file, summary):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        for key, value in summary.items():
            if isinstance(value, list):  # Handle outliers list
                value = ', '.join(map(str, value))
            writer.writerow([key, value])

def process_csv(file_path):
    rows = read_csv(file_path)
    summary = five_number_summary(rows)
    write_summary_to_csv('exp6_output.csv', summary)

input_file = 'exp2_input.csv'
process_csv(input_file)

print("Summary written to exp6_output.csv")
