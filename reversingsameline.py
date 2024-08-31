no = 1234567
reverse = 0
while no>0:
    rem = no%10
    reverse = (reverse*10) + rem             ### ora line la 7654321 nu varum
    no = no//10
    
else:
    print(reverse)
