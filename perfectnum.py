
no=28
div = 1
sum = 0
while div<no:
    if no%div==0:
        sum+=div
        print(div)
    div+=1
  
if no == sum:
    print("Perfect")
else:
    print("Not perfect")

'''

def find_perfect(num):
    div = 1
    sum = 0
    while div<num:
        if num%div==0:
            sum+=div
        div+=1
    return sum

no = int(input("Enter no. "))
if no == find_perfect(no):
    print("Perfect")
else:
    print("Not perfect")
'''



