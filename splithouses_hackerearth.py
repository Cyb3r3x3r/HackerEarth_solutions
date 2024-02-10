def divide_village(village):
    houses = spaces = [i for i in range(n) if village[i] == 'H']
    distances = [houses[i+1] - houses[i] - 1 for i in range(len(houses) - 1)]
    
    if 0 in distances:
        print("NO")
        return
    else:
        print("YES")
    spaces = [i for i in range(n) if village[i] != 'H']
 
    for i in range(len(spaces)):
        idx = spaces[i]
        village[idx] = 'B'
    
    print(''.join(village))
    
    
n = int(input())
village = input()
divide_village(list(village))