SQUARE INSIDE A SQUARE :

code :

print("Enter the length of the square")
n=int(input())
k=n-3
for i in range(n):
    for j in range(2*n):
        if (i==0 or i==n-1) and j%2==0:
            print('*',end="");
        elif j==0 or j==2*(n-1):
            print('*',end="")
        elif (i==2 or i==k) and (j>=4 and j<=2*(n-3) and j%2==0):
            print('*',end="")
        elif (i>2 and i<k) and (j==4 or j==2*(n-3)):
            print('*',end="")
        else:
            print(" ",end="")
    print()

Output :

Enter the length of the square
7
* * * * * * * 
*           * 
*   * * *   * 
*   *   *   * 
*   * * *   * 
*           * 
* * * * * * * 
-
