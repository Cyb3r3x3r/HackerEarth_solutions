name = input()
#DDXDDD-DD
if(name[2]=='A' or name[2]=='E' or name[2]=='I' or name[2]=='O' or name[2]=='U' or name[2]=='Y'):
    print("invalid")
else:
    check = int(name[0])+int(name[1])
    if(check%2==0):
        check = int(name[3])+int(name[4])
        if(check%2==0):
            check = int(name[4])+int(name[5])
            if(check%2==0):
                check = int(name[7])+int(name[8])
                if(check%2==0):
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            print("invalid")
    else:
        print("invalid")