def distance(point1, point2):
  squared_difference = 0
  for i in range(len(point1)):
    squared_difference += (point1[i] - point2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknownPoint, dataset, k):
  distances = []
  for title in dataset:
    distance_to_point = distance(unknownPoint, dataset[title])
    distances.append([distance_to_point, title])
  
  distances.sort()
  neighbors = distances[:k]
  return neighbors
