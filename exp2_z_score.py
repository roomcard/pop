import csv

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        rows = [float(row[0]) for row in reader]
    return rows

def z_score_normalization(data):
    mean_val = sum(data) / len(data)
    
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5

    normalized_data = [(x - mean_val) / std_dev for x in data]
    
    return normalized_data

def process_csv(file_path, output_file):
    rows = read_csv(file_path)
    normalized_data = z_score_normalization(rows)
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for original, norm_value in zip(rows, normalized_data):
            writer.writerow([original, norm_value])

input_file = 'exp2_input.csv'
output_file = 'exp2_zscore_output.csv'
process_csv(input_file, output_file)