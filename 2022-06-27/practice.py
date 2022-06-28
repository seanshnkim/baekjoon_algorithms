toAdd = [(0,0,-1), (0,-1,-1), (0,-1,0), (-1,0,0), (-1,-1,0), (-1,0,-1), (-1,-1,-1)]

a,b,c = 3,2,1

for i in range(7):
    x,y,z = map(sum, zip((a,b,c),toAdd[i]))
    print(x,y,z)