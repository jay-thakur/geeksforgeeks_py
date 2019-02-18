"""
Given a number X and another number Y . There are a total  N cycles ,  and alternatively we perform operation on each number . In each cycle , we multiply the number by 2 . Starting with X .

Suppose after all the N cycles, the number X has become W and  number Y has become Z . You have to calculate the division of the maximum number among W and Z by the minimum number among W and Z .

Input:
The first line of the input contains an integer T denoting the number of test cases. The description of each testcase follows. Each test case contains a single line with 3 integers X , Y , and N .

Output:
For each test case output a new line with a single integer which should be the answer.

Constraints:
1 ≤ T ≤ 100
1 ≤ X ≤ 10000000
1 ≤ Y ≤ 10000000
1 ≤ N ≤ 10000000

Example:
Input:
2
1 2 1
3 2 3
Output:
1
3
Explanation:
In the first testcase ( only one cycle ), the initial numbers are ( X = 1, Y = 2). There is only one turn. In this turn X is multiplied by 2. Hence, we get (X = 2, Y = 2). Therefore W = 2, and Z = 2 . max ( W , Z ) / min ( W ,  Z ) =  2 / 2  = 1. Hence the first output is 1.

In the second testcase, the initial numbers are (X = 3, Y = 2) . There three turns. In the first cycle X is multiplied by 2 . So, we get ( X = 6, Y = 2 ) . In the second cycle Y ( Y = 2)  multiplies his number by 2. Hence, we get  ( X = 6,  Y = 4 ) . In the third cycle  X ( X = 6) is multiplied by 2. So, we get (X = 12, Y = 4) . As N = 3 , and we are completed with 3 cyles ,  therefore W = 12, and Z = 4 .
max ( W ,  Z ) / min ( W , Z ) = 12 / 4 = 3. Hence the second output is 3.
"""
import math


def the_cycle_game(x, y, n):
    w = x * (2 ** math.ceil(n / 2))
    z = y * (2 ** (n // 2))

    if w > z:
        return w // z
    else:
        return z // w


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        x, y, n = [int(i) for i in input().split()][0:3]
        print(the_cycle_game(x, y, n))
