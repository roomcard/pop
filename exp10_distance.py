import csv
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Read data from CSV file
input_file = "data.csv"
output_file = "output.csv"
points = []

with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header
    for row in csvreader:
        x = int(row[1])
        y = int(row[2])
        points.append((x, y))

n = len(points)
x_sum = sum(point[0] for point in points)
y_sum = sum(point[1] for point in points)

# Calculate midpoint
mid_x = x_sum / n
mid_y = y_sum / n
print(f"Mid Point: ({mid_x}, {mid_y})")

# Write output to CSV
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([" ", "p1", "p2", "p3", "p4", "p5", "C"])

    for i in range(n):
        row = [f"p{i + 1}"]
        for j in range(n):
            if i == j:
                row.append("0")
            else:
                dis = distance(points[i][0], points[i][1], points[j][0], points[j][1])
                row.append(f"{dis:.2f}")
        csvwriter.writerow(row)

    csvwriter.writerow(["C"])
    
    # Calculate distance of each point from midpoint and find the nearest point
    min_distance = float('inf')
    nearest_point_index = -1
    
    for i, (x, y) in enumerate(points):
        dist = distance(mid_x, mid_y, x, y)
        print(f"Distance of p{i + 1} from centre: {dist}")
        if dist < min_distance:
            min_distance = dist
            nearest_point_index = i
            nearest_point = (x, y)
        csvwriter.writerow([f"{dist:.2f}"])

    print(f"Nearest Distance: {min_distance}")
    print(f"Nearest point from Centre is: p{nearest_point_index + 1}")

    csvwriter.writerow([" "])

    # Calculate and write distances from the new center
    csvwriter.writerow([" ", "p1", "p2", "p3", "p4", "p5"])
    for i in range(n):
        row = [f"p{i + 1}"]
        for j in range(n):
            if i == j:
                row.append("0")
            else:
                dis = distance(points[i][0], points[i][1], points[j][0], points[j][1])
                row.append(f"{dis:.2f}")
        csvwriter.writerow(row)

    row = [f"p{nearest_point_index + 1}(New Center)"]
    for x, y in points:
        dis = distance(nearest_point[0], nearest_point[1], x, y)
        print(f"Distance of p{points.index((x, y)) + 1} from p{nearest_point_index + 1}: {dis}")
        row.append(f"{dis:.2f}")
    csvwriter.writerow(row)
