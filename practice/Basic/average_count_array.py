"""
You are given an integer ' n ' which denote the number of elements in an array a[ ] and an integer ' x '. You have to calculate the average of element a[i] and x and find out if that number exist in array or not. Do it for all the elements of array and store the count result in another array for each index i.

Input:

First line contains integer t denoting number of test cases. The next subsequent lines contain numbers ' n ' and ' x '. Elements of array a[ ].


Output:

You have to print the resultant array in which you have to calculate the number of times the average of a[i] and x occurs in the array for each index i.


Constraints:

0 < t < 100

0 < n < 100

0 < x < 100

0 < a[i] < 100


Example:

Input:

2
5 2
2 4 8 6 2
6 3
9 5 2 4 0 3

Output:

2 0 0 1 2

0 1 1 1 0 1

Explanation:

For eg 1: value of n is 5 and that of x is 2. The array is 2 4 8 6 2. We take x i.e. 2 and take average with a[0]
whch is equal to 2. We found 2 resides in array at two positions (1st and 5th element) thus storing 2 in another array
at 0th index.Similarly do for all elements and store the count in second array.
"""


def average_count_array(arr, x):
    ans = []
    for i in arr:
        ans.append(arr.count((i + x) // 2))
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:n]
        print(*average_count_array(arr, x))
