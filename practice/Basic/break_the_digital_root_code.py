"""
Junpei has been abducted by the mastermind Zero and has been put in a locked cell. The door of the cell has been locked with a weird mechanism. There is an input panel on the door. The input panel has buttons labeled from 0-9. The panel screen shows a digit x and a number N. Now, Junpei has to enter N numbers (starting from 1) whose digital root is equal to the digit x. Can you help Junpei break the code by entering all correct numbers? Remember, the bomb will go off if you enter a wrong number!
The digital root of a non-negative number can be obtained by repeatedly summing the digits of the number until we reach to a single digit. Example: DigitalRoot(98)=9+8=>17=>1+7=>8(single digit!)

Input: First line contains an integer denoting the test cases 'T'. Every test case contains an integer value N and another integer x. N and x are separated by spaces.
Output: Print N numbers in a single line as the output. The numbers should be separated by spaces. The numbers are printed in ascending order. The maximum difference between two successive elements should not exceed 9.
Constraints:
1<=N<=10000
1<=x<=9
Example:

Input:
2
10 9
20 3
Output:
9 18 27 36 45 54 63 72 81 90
3 12 21 30 39 48 57 66 75 84 93 102 111 120 129 138 147 156 165 174
"""


def break_the_digital_root_code(n, x):
    return list(str(x + 9 * i) for i in range(n))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = [int(i) for i in input().split()][0:2]
        print(*break_the_digital_root_code(n, x))
