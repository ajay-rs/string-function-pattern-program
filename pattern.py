'''
row=1
while row<=9:
    col=1
    while col<=9:
        if row==1 or row==9:
            print("*",end=" ")
        elif col==5:
            print("*",end=" ")                                           #(I)
        else:
            print(" ",end=" ")
        col=col+1    

    print()
    row=row+1


row=1
while row<=9:
    
    col=1
    while col<=9:
        if row in (1,5,9):
            print("*",end=" ")
        elif col==1:
            print("*",end=" ")                                          #(E)
            
        else:
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1
    


row=1
while row<=9:
    col=1
    while col<=9:
        if row==col and col<=5:
            print("*",end=" ")
        elif col+row==10 and row<=5:
            print("*",end=" ")                               #(Y)
        elif col==5 and row>=5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1





row=1
while row<=9:
    col=1
    while col<=9:
        if row==col and col<=5:                           #(M)
            print("*",end=" ")
        elif col+row==10 and row<=5:
            print("*",end=" ")
        elif col in (1,9):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1



row=1
while row<=9:
    col=1
    while col<=9:
        if row==col and col>=5:                           #(w)
            print("*",end=" ")
        elif row+col==10 and row>=5:
            print("*",end=" ")
        elif col in (1,9):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1



row=1
while row <=9:
    col=1
    while col<=9:
        if row in (1,5):
            print("*",end=" ")
        elif col==1 or col==9:
            print("*",end=" ")
        else:                                                                                         #(A)
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1



row=1
while row<=9:
    col=1
    while col<=9:
        if row in (1,5,9):
       
            if col>=1 and col<9:
            print("*",end=' ')
          
        elif col==1 or col==9: 
            print("*",end=" ")
        else:                                                                                         #(B)
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1      


row=1
while row<=9:
    col=1
    while col<=9:
        if row==1:
            print("*",end=" ")
        elif col==5:                                                           #(T)
            print("*",end=" ")

        else:                                                                                         
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1      






row=1
while row<=9:
    col=1
    while col<=9:
        if row==1:
            print("*",end=" ")
        elif col==5 :                                                           #(J)
            print("*",end=" ")
        elif row==9 and col<=5:
            print("*",end=" ")

        else:                                                                                         
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1     



row=1
while row<=9:
    col=1
    while col<=9:
        if row==col:
            print("*",end=" ")
        elif col+row==10:                                                           #(X)
            print("*",end=" ")

        else:                                                                                         
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1     
'''

row=1
while row<=9:
    col=1
    while col<=9:
        if row==col and col<=5:
            print("*",end=" ")
        elif col+row==10 and row<=5 :                                                           #(Y)
            print("*",end=" ")
        elif col==5 and row>=5:
            print("*",end=" ")
        else:                                                                                         
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1     
'''
row=1
while row<=9:
    col=1
    while col<=9:
        if row==1 or row==9:
            print("*",end=" ")
        elif col+row==10  :                                                           #(z)
            print("*",end=" ")
       
        else:                                                                                         
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1 
'''   
