# while value != 0:

def Loop(i):
    i = +1
    userKey = input("Enter user Key:")
    uservalue = input("Enter user value:")
    # both = [userKey + ":" + uservalue]
    # print(both)
    if i == 0:
        both = [userKey+":"+uservalue]
        print(both)
    else:
        both.extend(both)
    print("Enter 0 to exit OR enter any other key to continue")
    value = input()
    i = i +1
    if value == 0:
        print(both)
        for j in range(len(both)):
            print(both[j])
        exit()
    else:
        Loop()
Loop()



## While loop
#
# def loop(user):
#     for a, b in user.items():
#         print(a,":",b)
#
# UserDetails = {}
# value = 1
# while value != 0:
#         UserKey =input("Enter user Key:")
#         UserValue =input("Enter user value:")
#         UserDetails[UserKey] = UserValue
#         value = input("Enter 0 to exit or press any key to contine...")
# loop(UserDetails)
# input()

