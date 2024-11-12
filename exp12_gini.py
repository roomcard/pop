import math
import csv

def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def entropy(data, target_attr):
    val_freq = {}
    data_entropy = 0.0
    
    for record in data:
        if record[target_attr] in val_freq:
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]] = 1.0
    
    for freq in val_freq.values():
        prob = freq / len(data)
        data_entropy += -prob * math.log2(prob) if prob > 0 else 0
    
    return data_entropy

def info_gain(data, attr, target_attr):
    val_freq = {}
    subset_entropy = 0.0
    
    for record in data:
        if record[attr] in val_freq:
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0
    
    for val in val_freq.keys():
        subset_data = [record for record in data if record[attr] == val]
        val_prob = len(subset_data) / len(data)
        subset_entropy += val_prob * entropy(subset_data, target_attr)
    
    total_entropy = entropy(data, target_attr)
    
    return total_entropy - subset_entropy

def gini_index(data, attr, target_attr):
    val_freq = {}
    gini = 0.0
    
    for record in data:
        if record[attr] in val_freq:
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    for val in val_freq.keys():
        subset_data = [record for record in data if record[attr] == val]

        subset_gini = 1.0
        val_prob = len(subset_data) / len(data)
        
        target_freq = {}
        
        for record in subset_data:
            if record[target_attr] in target_freq:
                target_freq[record[target_attr]] += 1.0
            else:
                target_freq[record[target_attr]] = 1.0
        
        for freq in target_freq.values():
            prob = freq / len(subset_data)
            subset_gini -= prob ** 2
        
        gini += val_prob * subset_gini
    
    return gini

file_name = 'exp4_infogain.csv'
data = read_csv(file_name)

target_attribute = input("Enter the target attribute (e.g., 'play'): ")

attributes = list(data[0].keys())
attributes.remove(target_attribute)

print(f"Calculating Information Gain and Gini Index for each attribute against the target '{target_attribute}':\n")
for attribute in attributes:
    gain = info_gain(data, attribute, target_attribute)
    gini = gini_index(data, attribute, target_attribute)
    
    print(f"Attribute: {attribute}")
    print(f"  Information Gain: {gain:.4f}")
    print(f"  Gini Index: {gini:.4f}\n")