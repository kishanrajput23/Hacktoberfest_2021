Example Input:
5

Output:
* * * * * * * * * * 
* * * * * * * * 
* * * * * * 
* * * * 
* * 
* * 
* * * * 
* * * * * * 
* * * * * * * * 
* * * * * * * * * * 

//python program

n=5
m=n*2
ast="* "
for i in range(m,0,-2):
    print(i*ast)
for j in range(2,m+1,2):
    print(j*ast)




