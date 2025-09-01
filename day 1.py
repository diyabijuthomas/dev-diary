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

#4
#sort a list of dictionaries 
a=[{"ravi":56},{"savu":80},{"Akhil":58}]
#flatten the list of dictionaries into a single dictionary instead of list
flat={k:v for d in a for k,v in d.items()}
sorted_names=sorted(flat,key=flat.get)
print(sorted_names)

#OR
scores={}
for item in a:
    for name, score in item.items()z:
        scores[name]=score
sorted_names=sorted(score,key=score.get)

#5 array's elements 1  unit to the left. The elements that fall off the left end reappear at the right end. Given an integer d, rotate the array that many steps to the left and return the result.

# STDIN      Function
# -----      --------
# 5 4         n = 5 d = 4
# 1 2 3 4 5  arr = [1, 2, 3, 4, 5]
# Sample Output

# 5 1 2 3 4
def rotateLeft(d, arr):
    new=[]
    new=arr[d:]
    for i in range (d):
        new.append(arr[i])
    arr=new
    return arr

#6
def matchingStrings(stringList, queries):
    # Write your code here
    result=[]
    for query in queries:
        s=0
        for stri in stringList:
            if stri==query:
                s+=1
        result.append(s)
    return result

#7 Timeout error is there
# STDIN       Function
# -----       --------
# 5 3         arr[] size n = 5, queries[] size q = 3
# 1 2 100     queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# 2 5 100
# 3 4 100
# Sample Output

# 200

def arrayManipulation(n, queries):
    arr=[0 for _ in range (n)]
    for query in queries:
        start,end,val=query
        for i in range(start-1,end):
            arr[i]+=val
    for i in arr:
        if i>high:
            high=i
    return high

max(arr)- can also find the highest

