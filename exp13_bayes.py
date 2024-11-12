# import csv

# def read_csv_data(file_name):
#     data_points = []
#     with open(file_name, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             data_points.append(row)
#     return data_points

# def calculate_class_probabilities(data):
#     total_count = len(data)
#     class_counts = {}
#     for row in data:
#         label = row[-1]
#         if label not in class_counts:
#             class_counts[label] = 0
#         class_counts[label] += 1
    
#     class_probabilities = {label: count / total_count for label, count in class_counts.items()}
#     return class_probabilities

# def calculate_feature_probabilities(data):
#     feature_counts = {}
#     total_count = len(data)
#     for row in data:
#         label = row[-1]
#         if label not in feature_counts:
#             feature_counts[label] = {}
        
#         for i in range(len(row) - 1):
#             feature = row[i]
#             if feature not in feature_counts[label]:
#                 feature_counts[label][feature] = 0
#             feature_counts[label][feature] += 1

#     feature_probabilities = {}
#     for label, features in feature_counts.items():
#         feature_probabilities[label] = {feature: count / total_count for feature, count in features.items()}

#     return feature_probabilities

# def classify(instance, class_probabilities, feature_probabilities):
#     max_prob = -1
#     best_class = None
#     for label, class_prob in class_probabilities.items():
#         prob = class_prob
#         for feature in instance:
#             feature_prob = feature_probabilities.get(label, {}).get(feature, 1 / (len(instance) + 1))
#             prob *= feature_prob
#         if prob > max_prob:
#             max_prob = prob
#             best_class = label
#     return best_class

# def main():
#     file_name = 'exp13_input.csv'
#     data_points = read_csv_data(file_name)
    
#     class_probabilities = calculate_class_probabilities(data_points)

#     feature_probabilities = calculate_feature_probabilities(data_points)

#     while True:
#         input_instance = input("Enter the features separated by commas (or 'exit' to quit): ")
#         if input_instance.lower() == 'exit':
#             break
#         instance = input_instance.split(',')
#         predicted_class = classify(instance, class_probabilities, feature_probabilities)
#         print(f"The predicted class is: {predicted_class}")

# if __name__ == "__main__":
#     main()

import csv

def calculate_prior(data, target_attr):
    prior = {}
    total = len(data)

    label_counts = {}

    for row in data:
        label = row[target_attr]
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1

    for label in label_counts:
        prior[label] = label_counts[label] / total
        print("priority prob for label" ,label)
        print(prior[label])
    return prior

def calculate_likelihood(data, target_attr, features):
    likelihood = {}
    labels = set()
    
    for row in data:
        labels.add(row[target_attr])

    # print(labels)
    for label in labels:
        likelihood[label] = {}
        
        subset = []
        for row in data:
            if row[target_attr] == label:
                subset.append(row)

        # print(subset)
        for feature in features:
            likelihood[label][feature] = {}
            
            unique_values = set()

            for row in subset:
                unique_values.add(row[feature])

            for value in unique_values:
                count = 0
                for row in subset:
                    if row[feature] == value:
                        count += 1  
                likelihood[label][feature][value] = count / len(subset)
    return likelihood

def bayesian_classification(data, target_attr, new_instance):

    prior = calculate_prior(data, target_attr)
    features = data[0].keys() - {target_attr}
    likelihood = calculate_likelihood(data, target_attr, features)
    
    posteriors = {}
    
    for label in prior.keys():
        posteriors[label] = prior[label]

        print(f"\nCalculating for class '{label}':")
        
        for feature in features:
            if new_instance[feature] in likelihood[label][feature]:
                posteriors[label] *= likelihood[label][feature][new_instance[feature]]
                print(f"Feature: {feature}, Value: {new_instance[feature]}, Likelihood probability is : {likelihood[label][feature][new_instance[feature]]}")
            else:
                posteriors[label] *= 0
                print(f"Feature: {feature}, Value: {new_instance[feature]}, Likelihood: 0 (not in training data)")
    
    return posteriors

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def get_user_input(features):
    new_instance = {}
    for feature in features:
        value = input(f"Enter the value for {feature}: ")
        new_instance[feature] = value
    return new_instance

if __name__ == "__main__":

    file_path = 'exp13_input.csv'
    data = read_csv(file_path)
  
    target_attr = 'play'
    features = data[0].keys() - {target_attr}
    
    canwe_continue = True

    while canwe_continue:
        new_instance = get_user_input(features)
        posteriors = bayesian_classification(data, target_attr, new_instance)
        print("\nPosterior probabilities :")
        for label, probability in posteriors.items():
            print(f"Class '{label}': {probability :.2f}%")

        result = max(posteriors, key=posteriors.get)
        print(f"\nThe predicted class label  for the new instance {new_instance} is: {result}")

        canwe_continue = input("if continue press y ? (y/n): ") == 'y'