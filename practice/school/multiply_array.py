"""
Calculate the product of all the elements in an array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines . The first line of each test case contains an integer N.The second line of each test case contains N space separated integers denoting elements of the array A[ ].

Output:
For each test case in a new line print the product of all elements.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 10
1 ≤ A[i] ≤ 5

Example:
Input:
2
5
1 2 3 4 5
10
5 5 5 5 5 5 5 5 5 5

Output:
120
9765625
"""


def multiply_array(arr):
    result = 1
    for e in arr:
        result *= e
    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(multiply_array(arr))