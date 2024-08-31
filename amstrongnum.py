no = 153
no2 = no
armstrong = 0
while no>0:
    rem = no%10                                                                                      ### kudukura value 1*1*1=(1),,5*5*5=(125),3*3*3=(27)
    armstrong = armstrong + (rem*rem*rem)
    no = no//10
else:
    if armstrong == no2:
        print("Armstrong")
    else:
        print("Not Armstrong")


no=407
no2=no
am=0
while no>0:
    n=no%10
    am=am+(n*n*n)
    no=no//10
else:
    if no2==am:
        print("amstrong")
    else:
        print("not ams")
