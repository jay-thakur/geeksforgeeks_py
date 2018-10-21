"""
Ishaan has N candies with him. He wants to put them in packets. He can put 1 candy in the first packet, 2 candies in the second packet, 4 candies in the third and so on.
Calculate the minimum number of packets he needs to store all the candies if he fills the packets starting from the first packet.

Input :
First line of input contains a single integer T denoting the number of test cases.
The only line of each test case contains an integer N.
Output :
For each test case, print the required answer in a new line.

Constraints :
1 <= T <= 200
1 <= N <= 10^15

Example :
Input :
3
2
4
7
Output :
2
3
3

Explanation :
Case 1 :
Put 1 candy in first packet.
Put 1 candy in second packet.

Case 2 :
Put 1 candy in first packet.
Put 2 candies in second packet.
Put 1 candy in third packet.

Case 3 : 
Put 1 candy in first packet.
Put 2 candies in second packet.
Put 4 candy in third packet.
"""


def candy_packets(n):
    count = 0
    index = 1
    while index <= n:
        count = count + 1
        index = index * 2

    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(candy_packets(n))
