"""
Adam has N chocolates of unequal lengths.He wants that each chocolate should be of equal lengths.In order to do so,at each step,he picks two unequal length chocolates and takes their length difference 'd' and then he eats the bigger one and make it's length  'd'.He stops when all the chocolates are of equal length.Find the final length of all chocolates.

Input:
Input contains T test cases.The first line of each test case contains a single integer N, denoting the number of chocolates. The second line contains N positive integers(Ai), each separated by a single space denoting lengths of chocolates.

Output:
For each test case, output a single integer - the value of  lengths of all the chocolates when they are equal (and the game terminates), in a new line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ Ai ≤ 109

Example:
Input:
3
2
10 12
2
5 9
3
6 10 15
Output:
2
1
1

Explanation:

{10,12} -> {10,2} -> {8,2} -> {6,2} -> {4,2} -> {2,2}
{5,9} -> {5,4} ->{1,4} -> {1,3} -> {1,2} -> {1,1}
{6,10,15} -> {6,10,9} -> {6,4,9} -> {6,4,3} -> {2,4,3} -> {2,4,1} -> {2,2,1} -> {1,2,1} -> {1,1,1}  [Note:this is one way of eating chocolates ,there could be many..]
"""


from math import gcd


def chocolate_lengths(arr):
    a = arr[0]
    for i in range(1, len(arr)):
        a = gcd(a, arr[i])
    return a


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(chocolate_lengths(arr))
