def loop(data):
    for a, b in data.items():
        print(a,":",b)

UserDetails = {}
value = 1
while value != 0:
        UserKey =input("Enter user Key:")
        UserValue =input("Enter user value:")
        UserDetails[UserKey] = UserValue
        value = input("Enter 0 to exit or press any key to contine...")
loop(UserDetails)
input()

