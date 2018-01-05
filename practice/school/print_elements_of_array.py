"""
Given an array, print all its elements.

Input:

The first line of the input contains T denoting the total number of testcases. The first line of each testcase contains N denoting the size of array. The second line contains N space separated positive integers denoting the elements of array.

Output:

For each testcase, print all its element in new line.

Constraints:

1<=T<=20
1<=N<=100
1<=a[i]<=100

Example:
Input:
1
5
1 2 3 4 5

Output:
1 2 3 4 5
"""
def print_elements_of_array(elements):
    element_list = list(elements)
    for element in element_list:
        print(element, end=' ')
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        elements = [int(i) for i in input().split()][0:size]
        print_elements_of_array(elements)