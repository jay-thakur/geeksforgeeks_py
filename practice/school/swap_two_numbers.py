"""
Swap given two numbers and print them. (Try to do it without a temporary variable.)

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain two positive numbers a and b.

Output:
Print the 2 numbers after swapping.

Constraints:
1<=T<=30
1<=a<=1000
1<=b<=1000

Example:
Input:
2
20 30
12 32

Output:
30 20
32 12

"""


def swap_two_numbers(numbers):
    return numbers[1], numbers[0]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        numbers = [int(i) for i in input().split()][0:2]
        num1, num2 = swap_two_numbers(numbers)
        print(num1, num2)