"""
Given a time in the format of hh:mm (12-hour format) 0 < hh < 12, 0 <= mm < 60. The task is to convert it into words

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two space separated integers 'h' and 'm' denoting hours and minutes respectively.

Output:
Output the input time into words.

Constraints:
1<=T<=10^5
1<=h<=12
1<=m<=60

Example:
Input:
6
6 0
6 10
6 15
6 30
6 45
6 47

Output:
six o' clock
ten minutes past six
quarter past six
half past six
quarter to seven
thirteen minutes to seven
"""


def convert_to_word(hr, min):
    num_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen",
               "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six",
               "twenty seven", "twenty eight", "twenty nine", "past"]

    if min == 0:
        print(num_str[hr], "o' clock")
    elif min == 30:
        print("half past", num_str[hr])
    elif min == 45:
        print("quarter to", num_str[hr + 1])
    elif min == 15:
        print("quarter past", num_str[hr])
    elif min == 1:
        print(num_str[min] + "minutes past" + num_str[hr])
    elif min == 59:
        print(num_str[60 - min] + " minute to " + num_str[hr + 1])
    elif min > 30:
        print(num_str[60 - min] + " minutes to " + num_str[hr + 1])
    elif min < 30:
        print(num_str[min] + " minutes past " + num_str[hr])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        hr, min = [int(i) for i in input().split()][0:2]
        convert_to_word(hr, min)
