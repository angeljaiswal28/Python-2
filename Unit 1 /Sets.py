#Create and access set elements
set1 = {1, 2, 3, 4, 5}
print("Set1:", set1)  # Output: {1, 2, 3, 4, 5}
print("Element 3 in set1:", 3 in set1)  # Access: True

#Union of sets
set2 = {4, 5, 6, 7}
union_set = set1.union(set2)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

#Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Output: {4, 5}

#Difference of sets
diff_set = set1.difference(set2)
print("Difference set1 - set2:", diff_set)  # Output: {1, 2, 3}
