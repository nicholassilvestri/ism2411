# ISM2411 Lab 10
# Name: Nicholas Silvestri

# Reflection
# 1. The most surprising thing about Python lists is that they can be change after being created. I also learned that indexing makes it much easier to access specific items.
#
# 2. In a business class, I could use a Python list to organize sales figures instead of having to calculate each number manually. This would make calculating totals and averages a lot easier. 

#---Exercise 1: Build the list---
inventory=["pen","notebook","stapler","tape","marker"]

print("Exercise 1")
print(inventory)
print(len(inventory))

#---Exercise 2: Index Practice---
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory)//2])

#---Exercise 3: Slicing---
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#---Exercise 4: Modify---
print("\nExercise 4")

inventory.append("envelope")
print("After appending:", inventory)

inventory.remove("tape")
print("After removing: ", inventory)

inventory.sort()
print("After sorting: ", inventory)

#---Exercise 5: Tuple Comparison---
print("\nExercise 5")

coords=(40.7128, -74.0060)

try:
    coords[0]=99
except TypeError:
    print("Tuples are useful for coordinates because they are immutable, meaning they cannot be changed after being created. This ensures that the values remain constant and reliable for representing fixed data like geographical coordinates.")

print(coords)

#---Exercise 6: Average of a list of sales---
print("\nExercise 6")

sales=[100, 250, 75, 480, 200]

total=sum(sales)
count=len(sales)
average=total/count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

#---Exercise 7: Accumulator pattern---
print("\nExercise 7")

prices=[9.99, 14.99, 4.99, 24.99, 1.99]
discounted=[]
for price in prices:
    discounted.append(round(price*0.9,2))

print("Original prices:", prices)
print("Discounted prices:", discounted)

#---Exercise 8: Filter above threshold---
print("\nExercise 8")

sales=[340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales=[]

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales)/len(high_sales), 2))