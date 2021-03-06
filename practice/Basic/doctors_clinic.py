"""
A doctor opens up his clinic at 10:00 a.m. There are many patients visiting him for the checkup. Doctor examines only one patient at a time and gives 10 minutes to each patient. There is a waiting room outside the doctor’s clinic so that when a patient arrives and doctor is busy he waits in the waiting room. Patients start arriving from 11:00 a.m. and each new patient arrives at a time period of x minutes. You are given the total number of patients and at what time interval (in minutes) the next patients are arriving for each test case. You have to calculate for how much time (in minutes) the last patient needs to wait in the waiting room.

Input:

The first line of input contains the number of test cases T. The next subsequent lines denote the total number of patients and time interval (in minutes) in which the next patients are visiting.
Output:

You have to calculate the total time in minutes for which the last patient needs to wait in the waiting room.
Constraints:

0 < T < 100

0 < n < 100

0 < x < 30
Example:

Input:

5
4 5
5 3
6 5
7 6
8 2

Output:

15
28
25
24
56
"""


def doctors_clinic(n, x):
    return (n - 1) * (max(10, x) - min(10, x))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = [int(i) for i in input().split()][0:2]
        print(doctors_clinic(n, x))
