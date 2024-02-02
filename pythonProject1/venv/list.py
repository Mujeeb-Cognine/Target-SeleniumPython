# List
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
print(adj)
print(fruits)

# Printing a particular value from the list
print(adj[1])
print(fruits[1])

# concat values of two lists at desired index
print(adj[1]+fruits[1])

# joining two lists at desired index
print(adj[1:3]+fruits[1:3])

# joining two lists
print(adj+fruits)

# updating the values in the list
adj[1] = "small"
fruits[1] = "Orange"
print(adj)
print(fruits)
print(adj)

# Adding new values to the list

# length of the list
print(len(adj))
print(len(fruits))

# adding the length of two lists
print(len(fruits)+len(adj))

# nested list
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

# converting list to Dictionary


