
def find_fact(num):
    fact = 1
    while num>0:
        fact = fact * num
        num-=1
    return fact


def split(no):
    total = 0
    while no>0:
        rem = no%10 #5  4   1
        total = total + find_fact(rem)
        no=no//10
    return total

no = 145
result = split(no)
if no == result:
    print("Strong Number")
else:
    print("Not Strong Number")











'''

sum=0
num=145
temp=num
while(num):
    i=1
    f=1
    r=num%10
    num=num//10
while(i<=r):
    f=f*i
    i=i+1
    sum=sum+f
    num=num+i
  
if num==temp:
    print("strong")
else:
    print("not strong number")

'''


