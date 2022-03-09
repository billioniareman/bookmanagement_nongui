import usersql

print("hey user")
while True:
    print("for data insertion enter 1,\nfor data updation enter 2, \nfor data deletion enter 3, \nto see all data from  "
        "the table enter 4")
    a = int(input("enter your choice: "))
    if a == 1:
        usersql.insertion()
    elif a == 2:
        usersql.updation()
    elif a == 3:
        usersql.deletion()
    elif a == 4:
        usersql.seeall()
    else:
        print("invalid response")
