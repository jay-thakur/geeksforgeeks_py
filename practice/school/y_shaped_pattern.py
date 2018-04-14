"""
Print a ‘Y’ shaped pattern from asterisks in N number of lines.

Note: N is even.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line contanining an integer N.

Output:
Corresponding to each test case,in a new line, print Y shaped pattern from asterisks in a single line considering spaces.

Constraints:
1 ≤ T ≤ 100
4 ≤ N ≤ 200

Example:
Input
2
4
8
Output

*   * * *   *    *
*       * *     *   *   *     * *       *        *        *        *
Explanation:

For the 1st test case where N = 4

*   *
 * *
  *
  *
The above is the proper Y shaped pattern for the test case, but when printed in a single line it becomes as shown in the output.
Please mind there are 2 spaces after the single * in the last row which has to be printed in single line also.
"""


def draw_y_shape_pattern(n):
    n //= 2
    for i in range(0, n):
        print(" " * i + "*" + " " * (2 * n - 1 - 2 * i) + "*" + " " * i, end="")
    for i in range(0, n):
        print(" " * n + "*" + " " * n, end="")
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        draw_y_shape_pattern(n)
