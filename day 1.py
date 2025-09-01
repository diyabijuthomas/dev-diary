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
better approach
def hourglassSum(arr):
    max_hourglass = float('-inf')  # Handles negative sums

    for i in range(4):  # 0 to 3
        for j in range(4):  # 0 to 3
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass = top + middle + bottom

            if hourglass > max_hourglass:
                max_hourglass = hourglass

    return max_hourglass
