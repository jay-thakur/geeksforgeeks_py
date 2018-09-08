"""
Given an increasing sequence a[], we need to find the K-th missing contiguous element in the increasing sequence which is not present in the sequence. If no k-th missing element is there output -1.

Input:
The first line consists of an integer T i.e. the number of test cases. The first line of each test case consists of two integers N and K.Next line consists of N spaced integers.

Output:
For each test case, print the Kth missing number if present otherwise print -1.

Constraints:
1<=T<=100
1<=N,K,A[i]<=105

Examples:
Input
2
5 2
1 3 4 5 7
6 2
1 2 3 4 5 6
Output
6
-1

Explanation:
#TestCase 1:
  K=2
We need to find the 2nd missing number in the array. Missing numbers are 2 and 6. So 2nd missing number is 6.
#Testcase 2:
K=2
We need to find the 2nd missing number in the array. As there is no missing number, hence the output is -1.
"""


def k_th_missing_element(arr):
    original_list = [x for x in range(arr[0], arr[-1] + 1)]
    num_list = set(arr)
    return list(num_list ^ set(original_list))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:n]

        missing_numbers_list = k_th_missing_element(arr)

        if len(missing_numbers_list) < k:
            print(-1)
        else:
            print(missing_numbers_list[k - 1])
