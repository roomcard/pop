import math
import csv

def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    # print(data)
    return data

def entropy(data, target_attr):
    val_freq = {}
    data_entropy = 0.0

    for record in data:
        if record[target_attr] in val_freq:
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]] = 1.0
    # print(val_freq)
    # print("End\n")
    for freq in val_freq.values():
        data_entropy += (-freq / len(data)) * math.log2(freq / len(data))
    return data_entropy

def info_gain(data, attr, target_attr, total_entropy):
    val_freq = {}
    subset_entropy = 0.0
    
    for record in data:
        if record[attr] in val_freq:
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    for val in val_freq.keys():
        val_prob = val_freq[val] / len(data)
        subset_data = [record for record in data if record[attr] == val]
        current_subset_entropy = entropy(subset_data, target_attr)
        print(f'Subset Entropy for {attr}={val}: {current_subset_entropy}')
        subset_entropy += val_prob * current_subset_entropy

    return total_entropy - subset_entropy

def print_probabilities(data, target_attr):
    val_freq = {}
    for record in data:
        if record[target_attr] in val_freq:
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]] = 1.0

    for val in val_freq.keys():
        print(f'Probability of {val}: {val_freq[val] / len(data)}')

file_name = 'exp4_infogain.csv'
data = read_csv(file_name)
target_attribute = input("Enter the target attribute (e.g., 'play'): ")
attributes = data[0].keys()
# print(attributes)

total_entropy = entropy(data, target_attribute)
print(f'Total Entropy for {target_attribute}: {total_entropy}')

for attribute in attributes:
    if attribute != target_attribute:
        gain = info_gain(data, attribute, target_attribute, total_entropy)
        print(f'Information Gain for {attribute}: {gain}')

print("\nProbabilities for each condition:")
print_probabilities(data, target_attribute)