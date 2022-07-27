# 2022-06-25(June 25th, 2022), Sehyun Kim

# a=[0]*2000005
# b=map(int,open(0))
# next(b)
# ans=[]
# for i in b:
#     a[i]=1
# for i in range(-1000000,1000001,1):
#     if a[i]:
#         ans.append(str(i))
# print("\n".join(ans))

# 뭔 뜻인지...next?
b = map(int, open(0))
next(b)
for i in b:
    print(i)