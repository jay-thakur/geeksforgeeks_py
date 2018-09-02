"""
Katty plays a lottery game -"Choose a number and win money" ,in which, a person playing a game has to select a number N and he/she will be awarded some money in Rupees accordingly.Some of the observations of selecting a number N and money awarded(M) are:-

N: 1   2   3   4   5   6   7   8   9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24 ..........

M: 3   2   1   6   5   4   3   2   1   12   11   10   9     8     7      6      5     4     3    2     1    24  23  22...............

i.e. if a Katty selects a number N=1,she gets M=Rs 3,if N=2,M=Rs 2,if N=3 ,M=Rs 1 and so on..

Input:
First line of input contains a single integer T denoting the number of test cases.The only of each test case contains an integer N denoting number chosen by Katty.

Output:
For each test case, print an integer M denoting the money won by Katty on chosing a  number N.

Constraints:
1<=T<=100
1<=N<=109

Example:
Input:
3
30
26
40
Output:
16
20
6
"""


def lottery_money(n):
    count = 3
    while n > count:
        n -= count
        count *= 2
    return count - n + 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(lottery_money(n))
