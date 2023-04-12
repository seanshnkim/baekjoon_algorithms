import sys
input = sys.stdin.readline

H, W = map(int, input().split())


def simulate(height, width):
    cnt_turn = 0
    end_loc = [0, 0]
    
    if height < width:
        smaller = height
        greater = width
        is_horizontally_long = True
    elif height > width:
        smaller = width
        greater = height
        is_horizontally_long = False
    
    # if height == width:
    else:
        if height == 2:
            cnt_turn = 2
            end_loc = [1, 0]

        elif height % 2 == 0:
            cnt_turn = 4*(height//2-1)+2
            end_loc = [height//2, width//2-1]
        else:
            cnt_turn = 4*(height//2)
            end_loc = [height//2, width//2]
        
        end_loc[0] += 1
        end_loc[1] += 1
        return cnt_turn, end_loc

    if smaller % 2 == 0:
        if smaller == 2 and is_horizontally_long:
            cnt_turn = 2
            end_loc[0] += 1
        else:    
            while smaller > 2:
                smaller -= 2
                cnt_turn += 4
                end_loc[0] += 1
                end_loc[1] += 1
            
            if is_horizontally_long:
                cnt_turn += 2
            else:
                cnt_turn += 3
            
            end_loc[0] += 1
    
    else:
        while smaller > 1:
            smaller -= 2
            greater -= 2
            cnt_turn += 4
            end_loc[0] += 1
            end_loc[1] += 1
        
        cnt_turn += 3
        
        if is_horizontally_long:
            end_loc[1] += (greater-1)
        else:
            end_loc[0] += (greater-1)
    
    end_loc[0] += 1
    end_loc[1] += 1
    return cnt_turn, end_loc
        
    
cnt, [end_x, end_y] = simulate(H, W)
print(cnt)
print(end_x, end_y)