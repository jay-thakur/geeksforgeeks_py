"""
You are given an array A of size N. The array A consists of a permutation of the set {1, 2, 3, … , N} for some positive integer N. You have to start at the position which has 1 in the array and then travel to the position which has 2. Then from 2, you travel to 3 and so on till you reach the position which has N. When you travel from A[i] to A[j], the distance travelled is |i– j|.Your aim is to find the total distance you have to travel to reach N when you start from 1.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two lines of input. The first line contains an integer N, where N is the size of the array A[ ]. The second line contains N space separated integers which denote a permutation of the set  {1, 2, 3, … , N}.

Output:
For each test case, print the total distance travelled.

Constraints:
1 <= T <= 100
1 <= N <= 107
1<= Ai <= 107

Example :
Input:
2
5
5 1 4 3 2
6
6 5 1 2 4 3

Output :
7
8

Explanation:
Testcase1: The numbers and their respective indices are given below:
1->1
2->4
3->3
4->2
5->0
Total distance =|4-1|+|3-4|+|2-3|+|0-2| = 3+1+1+2 = 7
"""


def total_distance_travelled(arr, size):
    l1 = list(arr)
    for i in range(0, size):
        l1[arr[i] - 1] = i - 1

    sum = int(0)
    for i in range(1, size):
        sum = sum + abs(l1[i] - l1[i - 1])
    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(total_distance_travelled(arr, size))
