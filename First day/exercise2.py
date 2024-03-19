import random

fruits = ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]

print(random.choices(fruits, k = 3)) #with replacement

print(random.sample(fruits, 3)) #without replacement