"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
def main()
n=int(input("Enter the size of row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=' ')
    print()

"""
*   
* *   
* * *   
* * * *   
* * * * *   
"""
for i in range(5):
    for j in range(5):
        if(j<=i):
         print("*",end=' ')
    else:
        print(" ",end=' ')
    print()

"""
      * 
    * * 
  * * * 
* * * * 
"""
for i in range(5):
    for j in range(5):
        if j>=5-i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
"""
* * * * * 
* * * *   
* * *     
* *       
*  
"""  


n=int(input("Enter the row size of the pattern:"))
for row in range(1,n+1):
    print("* " * (6-row))
    
"""
* * * * * 
* * * *   
* * *     
* *       
*  
"""


n=int(input("Enter the row size of the pattern:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i+1:
            print("*",end=' ')
        else:
            print(" ",end=' ') 
    print()
    
    

"""
      *       
    * * *     
  * * * * *   
* * * * * * * 
"""


n=int(input("Enter the row size of the pattern:"))
x=int(input("Enter the column size of the patteen:"))
for i in range(1,n+1):
    for j in range(1,x+1):
        if j>=5-i and j<=3+i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
    
"""
* * * * * * * 
  * * * * *   
    * * *     
      *     
"""  

n=int(input("Enter the row size of the pattern:")) #4
x=int(input("Enter the column size of the patteen:")) #7
for i in range(1,n+1):
    for j in range(1,x+1):
        if j>=i and j<=8-i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
"""
* * * * * * * 
* * *   * * * 
* *       * * 
*           * 
"""
n=int(input("Enter the row size of the pattern:"))
x=int(input("Enter the column size of the patteen:"))
for i in range(1,n+1):
    for j in range(1,x+1):
        if j<=5-i or j>=3+i: 
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
    
"""
1       
1 2     
1 2 3   
1 2 3 4 

""" 
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print(j,end=' ')
        else:
            print(" ",end=' ')
    print()
  
"""
1 2 3 4 5 
1 2 3 4   
1 2 3     
1 2       
1    
  """  
n=int(input("Enter the row size of the pattern:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i+1:
            print(j,end=' ')
        else:
            print(" ",end=' ')
    print()
    
    
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(2*i-1):
        print("*",end=' ')
    print()
"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(2*i-1):
        print("*",end=' ')
    print()

"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""
n=int(input("Enter the number of row:"))
#upper piramid
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(2*i-1):
        print("*",end=' ')
    print()
#lower piramid
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(2*i-1):
        print("*",end=' ')
    print()
    
"""
  * * * * * * * 
    * * * * * 
      * * * 
        * 
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

"""
def diamond():
    n = int(input("Enter the number of rows: "))

    # upper pyramid
    for i in range(n-1, 0, -1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(2*i - 1):
            print("*", end=" ")
        print()

    # lower pyramid
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(2*i - 1):
            print("*", end=" ")
        print()


# function call
diamond()

"""
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
"""
def diamond_x1():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n+1):
        # spaces
        for j in range(n-i):
            print(" ", end=" ")

        # left side numbers (1 to i)
        for k in range(1, i+1):
            print(k, end=" ")

        # right side numbers (i-1 to 1)
        for l in range(i-1, 0, -1):
            print(l, end=" ")

        print()

diamond_x1()
