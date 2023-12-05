def person(data):
    for k, v in data.items():
        print(k, ":", v)

# mydata={'name':'Vamsi','age':27,'city':'Hyd'}
# person(mydata)


userdata = {}
e = 1
while e != '0':
    userkey = input("Enter user key :")
    uservalue = input("Enter user value :")
    userdata[userkey] = uservalue
    e = input("Enter 0 to exit or press any key to continue...")
    person(userdata)
    input()
