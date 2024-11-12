import csv

def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(int(row[0]))
    return data

def binning_by_median(data, bin_size):
    if bin_size == 0:
        return data
    
    if bin_size > len(data):
        print("Bin size is greater than the data size")
        return 

    data.sort()
    binned_data = []
    
    for i in range(0, len(data), bin_size):
        bin_data = data[i:i + bin_size]
        median = sorted(bin_data)[len(bin_data) // 2]
        binned_data.extend([median] * len(bin_data))
        
    return binned_data

def binning_by_mean(data, bin_size):
    if bin_size == 0:
        return data
    
    if bin_size > len(data):
        print("Bin size is greater than the data size")
        return 

    data.sort()
    binned_data = []
    
    for i in range(0, len(data), bin_size):
        bin_data = data[i:i + bin_size]
        mean = sum(bin_data) / len(bin_data)
        binned_data.extend([round(mean, 2)] * len(bin_data))
        
    return binned_data

def binning_by_boundaries(data, bin_size):
    if bin_size == 0:
        return data
    
    if bin_size > len(data):
        print("Bin size is greater than the data size")
        return 
    
    data.sort()
    binned_data = []
    
    for i in range(0, len(data), bin_size):
        bin_data = data[i:i + bin_size]
        min_val = bin_data[0]
        max_val = bin_data[-1]
        for value in bin_data:
            if abs(value - min_val) < abs(value - max_val):
                binned_data.append(min_val)
            else:
                binned_data.append(max_val)
                
    return binned_data

def write_csv(output_file, data, median_binned, mean_binned, boundaries_binned):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Original', 'Median Binned', 'Mean Binned', 'Boundaries Binned'])
        for original, median_bin, mean_bin, boundaries_bin in zip(data, median_binned, mean_binned, boundaries_binned):
            writer.writerow([original, median_bin, mean_bin, boundaries_bin])

if __name__ == "__main__":
    file_name = 'exp3_input.csv'
    output_file = 'exp3_output.csv'
    
    bin_size = int(input("Enter the number of bins you need to create: "))

    data = read_csv(file_name)

    median_binned = binning_by_median(data.copy(), bin_size)
    mean_binned = binning_by_mean(data.copy(), bin_size)
    boundaries_binned = binning_by_boundaries(data.copy(), bin_size)

    write_csv(output_file, data, median_binned, mean_binned, boundaries_binned)
    
    print(f"Binned data has been written to {output_file}")
