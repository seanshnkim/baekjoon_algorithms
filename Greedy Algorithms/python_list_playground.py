
def change_list_values(arr):
    arr[0] ^= 1
    arr[1] ^= 1
    arr[2] ^= 1


test_list = [0,1,1]
test_list_copy = test_list.copy()

change_list_values(test_list_copy)
print(test_list_copy)