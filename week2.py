# Step 1: Creating an empty list
my_list = []

# Step 2: Appending elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Inserting 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extending with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Removing the last element
my_list.pop()

# Step 6: Sorting in ascending order
my_list.sort()

# Step 7: Finding and printing index of 30
index_of_30 = my_list.index(30)

print("Final List:", my_list)
print("Index of 30:", index_of_30)
