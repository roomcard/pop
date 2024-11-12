import csv
from itertools import combinations

def get_itemsets(transactions, length):
    itemsets = set()
    for transaction in transactions:
        for itemset in combinations(sorted(transaction), length):
            itemsets.add(itemset)
    return itemsets

def get_frequent_itemsets(transactions, min_support, n):
    itemsets = []
    level = 1

    candidate_itemsets = get_itemsets(transactions, level)
    all_frequent_itemsets = {}

    while candidate_itemsets:
        itemset_count = {}

        for itemset in candidate_itemsets:
            itemset_count[itemset] = 0

        for transaction in transactions:
            for itemset in candidate_itemsets:
                if set(itemset).issubset(transaction):
                    itemset_count[itemset] += 1

        frequent_itemsets = {}
        for itemset, count in itemset_count.items():
            if count >= (min_support / 100) * n:
                frequent_itemsets[itemset] = count
                all_frequent_itemsets[itemset] = count

        if not frequent_itemsets:
            print("No frequent itemsets found for level", level)
            break

        print(f"\nFrequent itemsets (level {level}):")
        for item, count in frequent_itemsets.items():
            print(f"Itemset: {item}, Count: {count}")

        itemsets.append(frequent_itemsets)

        candidate_itemsets = set()
        frequent_items = set()

        for sublist in itemsets[-1].keys():
            for item in sublist:
                frequent_items.add(item)

        level += 1
        for itemset in combinations(frequent_items, level):
            candidate_itemsets.add(itemset)

    write_frequent_itemsets_to_csv('exp7_freq.csv', all_frequent_itemsets)
    return itemsets

def write_frequent_itemsets_to_csv(output_file, frequent_itemsets):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Itemset', 'Count'])
        for itemset, count in frequent_itemsets.items():
            writer.writerow([', '.join(itemset), count])

def calculate_confidence(rule, all_frequent_itemsets):
    """Calculate confidence for a given rule."""
    antecedent, consequent = rule
    antecedent_count = all_frequent_itemsets.get(frozenset(antecedent), 0)
    rule_count = all_frequent_itemsets.get(frozenset(antecedent.union(consequent)), 0)
    return rule_count / antecedent_count if antecedent_count > 0 else 0

def generate_association_rules(frequent_itemsets, min_confidence, all_frequent_itemsets):
    rules = []
    for itemset, count in frequent_itemsets.items():
        if len(itemset) < 2:
            continue
        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = set(antecedent)
                consequent = set(itemset) - antecedent
                if consequent:
                    confidence = calculate_confidence((frozenset(antecedent), frozenset(consequent)), all_frequent_itemsets)
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent, confidence))
    return rules

def write_association_rules_to_csv(output_file, rules):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for antecedent, consequent, confidence in rules:
            writer.writerow([', '.join(antecedent), ', '.join(consequent), confidence * 100])

def read_csv_transactions(file_path):
    transactions = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            transaction = set(item.strip() for item in row if item)
            transactions.append(transaction)
    return transactions

def main():
    file_path = 'exp7_apriori.csv'
    transactions = read_csv_transactions(file_path)
    n = len(transactions)
    min_support = float(input("Enter the minimum support percentage: "))
    
    frequent_itemsets = get_frequent_itemsets(transactions, min_support, n)

    min_confidence_percentage = float(input("Enter the minimum confidence percentage (0-100): "))
    min_confidence = min_confidence_percentage / 100
    
    all_frequent_itemsets = {frozenset(itemset): count for level in frequent_itemsets for itemset, count in level.items()}
    rules = generate_association_rules(all_frequent_itemsets, min_confidence, all_frequent_itemsets)
    
    write_association_rules_to_csv('exp8_assoc.csv', rules)

if __name__ == "__main__":
    main()

    print("Frequent itemsets written to exp7_freq.csv")
    print("Association rules written to exp8_assoc.csv")