#1 Reverse a list - a[::-1]

#2 
There are 16 hourglasses in a 6*6 array. The hourglass sum  is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in arr, then print the maximum  hourglass sum.

def hourglassSum(arr):
    # Write your code here
    n=[[0 for _ in range(4)]for _ in range(4)]
    for i in range (4):
        for j in range (4):
            n[i][j]=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
    max=float('-inf')
    for i in range (4):
        for j in range (4):
            if n[i][j]>max:
                max=n[i][j]
    return max
    
#better approach

def hourglassSum(arr):
    max_hourglass = float('-inf')  

    for i in range(4):  
        for j in range(4):  
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass = top + middle + bottom

            if hourglass > max_hourglass:
                max_hourglass = hourglass

    return max_hourglass
#note that u use float('-inf') to initiate max, since negative sum can be also max value

# #3 STDIN    Function
# -----    --------
# 2 5      size of arr[] n = 2, size of queries[] q = 5
# 1 0 5    queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1
# output 
# 7
# 3

def dynamicArray(n, queries):
    # Write your code here
    arr=[[] for _ in range (n)]
    lastAnswer=0
    result=[]
    for i in queries:
        q,x,y=i
        idx=(x ^ lastAnswer)%n
        if q==1:
            arr[idx].append(y)
        elif q==2:
            lastAnswer=arr[idx][y %len(arr[idx])]
            result.append(lastAnswer)
    return result

#major insight is that u can define the values in a list as a,b, c = i, effectively unpacking it

