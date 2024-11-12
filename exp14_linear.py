import csv

def mean(values):
    return sum(values) / len(values)

def linear_regression_coefficients(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    mean_xy = mean([x[i] * y[i] for i in range(len(x))])
    mean_x_squared = mean([x[i] ** 2 for i in range(len(x))])
    
    b1 = (mean_xy - mean_x * mean_y) / (mean_x_squared - mean_x ** 2)
    b0 = mean_y - b1 * mean_x
    return b0, b1

def read_csv(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x, y

def write_csv(filename, b0, b1):
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Intercept (b0)', 'Slope (b1)'])
        csv_writer.writerow([b0, b1])

def main():
    input_filename = 'exp14_input.csv'
    output_filename = 'exp14_output.csv'
    
    x, y = read_csv(input_filename)
    
    b0, b1 = linear_regression_coefficients(x, y)
    
    write_csv(output_filename, b0, b1)
    
    print(f"Intercept (b0): {b0}")
    print(f"Slope (b1): {b1}")

if __name__ == "__main__":
    main()
