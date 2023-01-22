from itertools import product

test_list_1 = [0,1,2]
test_list_2 = [3,4,5]
test_list_3 = [6,7]

for i in product(test_list_1, test_list_2, test_list_3):
    print(i) 
    '''
    (0, 3, 6)
    (0, 3, 7)
    (0, 4, 6)
    (0, 4, 7)
    ...
    '''

for i in product([test_list_1, test_list_2, test_list_3]):
    print(i) 
    '''
    ([0, 1, 2],)
    ([3, 4, 5],)
    ([6, 7],)
    '''
