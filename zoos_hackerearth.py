import sys
name = input()
size = len(name)
x = 0
y = 0
for a in range(size):
    if name[a]=='z':
        x = x +1
    elif name[a]=='o':
        y = y + 1
    else:
        sys.exit()
if 2*x==y:
    print("Yes")
else:
    print("No")