
no=9
no2=no*no
sum=0
while no2>0:
    a=no2%10
    sum=sum+a
    print(sum)                        # reminder
    no2=no2//10
if no==sum:
    print("it is neon")
else:
    print("not a neon")

'''

def neon(u,power):
    result=1
    while power>0:
        result=result*u
        power=power-1
    else:
        return result
def ajay(num):
    sum=0
    while num>0:
        da=num%10
        sum=sum+da
        num=num//10
    else:
        return sum
u=int(input("enter a neon number:"))
output=neon(u,2)
if u==ajay(output):
    print("its is neon")
else:
    print("not neon")   



     


def find_power(base, power):
    result = 1
    while power>0:
        result = result * base
        power-=1
    else:
        return result

def sum_of_digits(num):
    sum =0
    while num>0:
        sum = sum + num%10
        num = num//10
    else:
        return sum


no = 9
output = find_power(no,2)
if no == sum_of_digits(output):
    print(f'{no} is Neon Number')
else:
    print(f'{no} is not Not Neon')


'''





