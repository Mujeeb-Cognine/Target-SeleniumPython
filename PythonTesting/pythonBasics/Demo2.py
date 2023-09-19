
values = [1, 2, "Mujeeb", 4, 5]
# List is a data type that allows multiple values and can be different data types


print(values[0]) # 1
print(values[3]) # 4
print(values[-1]) # 5 -1 gives th last index
print(values[1:3]) # Printing from 2 index to 4 the index

values.insert(3,"Rahaman") # inserting the value at 3rd index
print(values) # [1, 2, 'Mujeeb', 'Rahaman', 4, 5]

values.append("End") #This appends the value at the end
print(values) # [1, 2, 'Mujeeb', 'Rahaman', 4, 5, 'End']

# Updating the value depending on index value
values[2] = "Mujju"
print(values) # [1, 2, 'Mujju', 'Rahaman', 4, 5, 'End']

# Deleting the value depeding on index value
del values[0]
print(values) # [2, 'Mujju', 'Rahaman', 4, 5, 'End']

#-----------------------------------------------------------------------------------------------------------------------
# List is mutable but Tuple is immutable else all others are same such that updations are not possible

#Tuple
val = (1, 2, "Mujeeb", 4.5)
print(val[1])

# val[2] = "Mujju" #No Possible

#-----------------------------------------------------------------------------------------------------------------------

# Dictonary

dic = {"a": 2, 4: "mujju", "c": "Hello World!"}

#Prints Not on index, but on the values assigned
print(dic[4])
print(dic["c"])

#How to create dictonary dynamically during run time {used in excell driven}

dict = {}

dict["firstname"] = "Mujeeb"

dict["lastname"] = "Rahaman"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])




