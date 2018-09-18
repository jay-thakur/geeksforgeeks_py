"""
Given a Binary Heap of size N, write a program to calculate the height of the Heap.

Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test case follows. The first line of each test case contains an integer N denoting the number of node in the Heap. Next line contains N space separated integers denoting the elements of the heap.

Output:
For each test case print the height of the Heap on a new line.

Constraints:
1<=T<=100
1<=N<=103

Example:
Input:
2
6
1 3 6 5 9 8
9
3 6 9 2 15 10 14 5 12
Output:
2
3
Explanation:
Testcase 1:

Input : N = 6
Output : 2
        (1)
       /    \
     (3)     (6)
    /  \    /
  (5)  (9) (8)
Testcase 2:

Input : N = 9
Output :
         (2)
      /       \
     (3)      (9)
    /  \     /   \
  (5) (15) (10)  (14)
  /  \
(6)  (12)
"""


import math


def height_of_heap(arr, size):
    return int(math.log(size, 2))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(height_of_heap(arr, size))
