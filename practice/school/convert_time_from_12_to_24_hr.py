"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00 AM on a 12-hour clock and 00:00:00 on a 24-hour clock. Noon is 12:00:00 PM on 12-hour clock and 12:00:00 on 24-hour clock.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a single string containing a time in 12-hour clock format(hh:mm:ss AM or hh:mm:ss PM.

Output:
Convert and print the given time in 24-hour format.

Constraints:
1<=T<=10^5
1<=hh<=12
1<=mm,ss<=59

Example:
Input:
2
07:05:45PM
01:05:45AM

Output:
19:05:45
01:05:45
"""


def convert_12_to_24(time):
    hr = time[0:2]
    session = time[8:10]
    if session == "PM" and int(hr) != 12:
        hr = str(int(hr) + 12)
    if int(hr) == 12 and session == "AM":
        hr = str("00")

    return hr + time[2:8]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        time = input()
        print(convert_12_to_24(time))
