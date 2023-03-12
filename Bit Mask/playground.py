some_list = [0,0,0,0,0,0,0,0,0]

flag = True
for i in range(len(some_list)):
    if some_list[i] == 1:
        flag = False
        break
if not flag:
    print("1이 없습니다")
    
    
