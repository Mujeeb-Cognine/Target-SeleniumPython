str = "mujeeb.rahaman@cognine.com"
str1 = "Service Based"
str2 = "mujeeb"

print(str)
print(str[1]) # To print only some character at mentioned index
print(str[0:6]) # To get the sub-string
print(str+str1) #Concatenation
print(str2 in str)# To check whether the string is present in or not
var = str.split(".") # Splitting the string
print(var)
print(var[0])
str3 = " Great "
print(str3.strip()) #Removing white spaces
print(str3.lstrip()) #Removing left white spaces
print(str3.rstrip()) #Removing right white spaces