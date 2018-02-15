"""
A file contains data as follows( Student name, marks in 3 subjects)
Shrikanth 20 50 60
Kiran 30 80 90
Find the student who has maximum average score.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the number of student.
The second line of each test case contains N input Student name and marks in 3 subject.

Output:

Print the student who has maximum average score and maximum average score(in int).

Note: If many students have the same average print the name of all these students in the same way as they appear in the input with space between each of the names and after that print the average marks.

Constraints:

1 ≤ T ≤ 10
1 ≤ N ≤ 15
1 ≤ s ≤ 10
1 ≤ marks ≤ 100

Example:

Input:
2
2
Shrikanth 20 30 10 Ram 100 50 10
3
Adam 50 10 40 Suresh 22 1 56 Rocky 100 90 10

Output:
Ram 53
Rocky 66
"""


def max_avg_score(no_of_student, student_record_list):
    max_avg = 0
    names = []
    for i in range(no_of_student):
        name = student_record_list[i * 4]
        avg_marks = int((int(student_record_list[i * 4 + 1]) + int(student_record_list[i * 4 + 2]) + int(
            student_record_list[i * 4 + 3])) / 3)
        if avg_marks > max_avg:
            names = [name]
            max_avg = avg_marks
        elif avg_marks == max_avg:
            names.append(name)
    print(' '.join(names), max_avg)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        no_of_student = int(input())
        student_record_list = list(map(str, input().split()))
        max_avg_score(no_of_student, student_record_list)