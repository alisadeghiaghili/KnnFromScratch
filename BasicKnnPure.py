def distance(point1, point2):
  squared_difference = 0
  for i in range(len(point1)):
    squared_difference += (point1[i] - point2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[:k]
  
  num_good = 0
  num_bad = 0
  
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
      
  if num_good > num_bad:
    return 1
  else:
    return 0
