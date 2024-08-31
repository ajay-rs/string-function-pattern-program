#reverseplusadd
no = 1234
sum_of_digits = 0
count=0
while no>0:
    i = no%10
    sum_of_digits = sum_of_digits + i
    no = no//10
    count=count+1
else:
    print(sum_of_digits)
    print(count)
'''





    











#Reversing given number
no = 1234567
reverse = 0
while no>0:
    rem = no%10
    reverse = (reverse*10) + rem             ### ora line la 7654321 nu varum
    no = no//10
    
else:
    print(reverse)


'''



