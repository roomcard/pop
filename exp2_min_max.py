import csv

input_file = 'exp2_input.csv'
data = []

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(float(row[0]))

min_val = min(data)
max_val = max(data)
new_min = int(input("Enter new min value:"))
new_max = int(input("Enter new max value:"))
normalized_data = [(((x - min_val) / (max_val - min_val))*(new_max-new_min))+new_min for x in data]

output_file = 'exp2_minmax_output.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for original, norm_value in zip(data, normalized_data):
        writer.writerow([original, norm_value])