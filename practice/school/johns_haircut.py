"""
Mr. John decides to have a haircut and goes to a barber shop. In the shop, he sees that there are n people waiting before him to have hair cut. He also notices a board which tells about diffrent types of haircut and time required for the hair designer to do that particular hair cut. Since John was very tired, he wanted to take a short nap before his turn. So he decides to set an alarm to wake up. Assuming each person is evenly likely for making a particular type of hair cut, help John to set alarm by telling him the floor of the expected time of wait.

NOTE: You can assume that when John sets alarm the hair designer starts his work for the first person

Input:

First line contains single integer 'T' denoting the number of test cases
First line of each test case contains two integers 'n' and 'x'
    n - number of people waiting before John
    x - number of types of haircut
Next line of the test-case contains x space separated integers, where ith integer denotes time taken for ith haircut


Output:

For each test case print the floor expected time of wait.


Constraints:

1 <= t <= 10
1 <= n,x <= 100000
1 <= time required for a haircut <= 1000000
Example:

INPUT:
1
1 2
10 8

OUTPUT:
9
"""


def johns_haircut(n, hair_cut):
    sum = 0
    for i in hair_cut:
        sum += i

    return int((sum / len(hair_cut)) * n)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = [int(i) for i in input().split()][0:2]
        hair_cut = [int(i) for i in input().split()][0:x]
        print(johns_haircut(n, hair_cut))
