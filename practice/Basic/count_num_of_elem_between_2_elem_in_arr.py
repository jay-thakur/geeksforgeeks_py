"""
Given an unsorted array and two elements num1 and num2. The task is to count the number of elements occurs between the given elements (excluding num1 and num2). If there are multiple occurrences of num1 and num2, we need to consider leftmost occurrence of num1 and rightmost occurrence of num2.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case contains an Integer N denoting size of array, second line contains N space separated array elements and third line contains two elements num1 and num2.

Output:
For each test case, print the count in new line.

Constraints:
1<=T<=200
2<=N<=105
1<=A[i],num1,num2<=105

Example:
Input:
2
5
4 2 1 10 6
4 6
4
3 2 1 4
2 4

Output:
3
1
"""


def count_num_of_elements_between_2_elements_in_a_array(arr, brr):
    a1 = arr.index(brr[0])
    a2 = len(arr) - arr[::-1].index(brr[1])
    return a2 - a1 - 2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m = int(input())
        arr = [int(i) for i in input().split()][0:m]
        brr = [int(i) for i in input().split()][0:2]
        print(count_num_of_elements_between_2_elements_in_a_array(arr, brr))
