import csv

def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    denominator = (denominator_x * denominator_y) ** 0.5
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

file_name = 'exp9_input.csv'
data = read_csv(file_name)

attribute_x = input("Enter the first attribute (e.g., 'column1'): ")
attribute_y = input("Enter the second attribute (e.g., 'column2'): ")

x = [float(row[attribute_x]) for row in data]
y = [float(row[attribute_y]) for row in data]

correlation = pearson_correlation(x, y)

print(f"Pearson Correlation Coefficient between {attribute_x} and {attribute_y}: {correlation}")