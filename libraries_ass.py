import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import math
import datetime

# Square root using math
print("Square root of 16:", math.sqrt(16))

# Current date
print("Today is:", datetime.date.today())

# Create an array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Mean and standard deviation
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Create a DataFrame (table)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Filter data
print("\nPeople older than 28:\n", df[df['Age'] > 28])


x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
print("Headers:", response.headers['content-type'])

