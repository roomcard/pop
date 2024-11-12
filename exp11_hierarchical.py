import csv
import math

def read_csv_data(file_name):
    data_points = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            point = [float(x) for x in row]
            data_points.append(point)
    return data_points

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def single_linkage(cluster1, cluster2):
    min_distance = float('inf')
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            distance = euclidean_distance(cluster1[i], cluster2[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

def agglomerative_clustering(data_points):
    clusters = [[point] for point in data_points]

    print(clusters)

    while len(clusters) > 1:
        min_distance = float('inf')
        cluster1_to_merge = 0
        cluster2_to_merge = 0

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                distance = single_linkage(clusters[i], clusters[j])
                if distance < min_distance:
                    min_distance = distance
                    cluster1_to_merge = i
                    cluster2_to_merge = j 
        print(f"Merging clusters: {clusters[cluster1_to_merge]} and {clusters[cluster2_to_merge]}")

        for point in clusters[cluster2_to_merge]:
            clusters[cluster1_to_merge].append(point)

        del clusters[cluster2_to_merge]
        print(f"Clusters after merge: {clusters}\n")
    return clusters[0]

def output_cluster(cluster):
    print("Final Cluster:")
    for point in cluster:
        print(point)

file_name = 'exp11_hier.csv'
data_points = read_csv_data(file_name)

print(data_points)

final_cluster = agglomerative_clustering(data_points)
output_cluster(final_cluster)