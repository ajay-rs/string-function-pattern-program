
def spy(no):
    sum=0
    while no>0:
        
        num=no%10
        sum=sum+num
        no=no//10
    return sum
def new(no):
    mul=1
    while no>0:
       
        u=no%10
        mul=mul*u
        no=no//10
    return mul
no=int(input("enter a number"))
a=spy(no)
b=new(no)

if  a==b:
    print("spy")
else:
    print("not a spy")




no=121
sum=0
mul=1
while no>0:
    l=no%10
    sum=sum+l
    mul=mul*l
    no=no//10
if sum==mul:
    print("spy number")
else:
    print("not a spy number")





def spynumber(num):
    sum1=0
    product=1
    while num>0:
        no=num%10
        sum1+=no
        product*=no
        num//=10
    return sum1, product
num=int(input("Enter the number:"))
sum1, product=spynumber(num)
print("sum:",sum1)
print("product:",product)
if sum1 == product:
    print("it is spy")
else:
    print("it is not spy" )




































