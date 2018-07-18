"""
A spider present at the bottom of the well of height H, needs to get out of it, using the slippery wall of the well. It decides to climb up the well, it goes up U metres and slips down D metres in one single step. So, in each step it covers (U-D) metres, and if the spider gets out of the well by covering U metres in the last step it doesn't slips back.
For example, if the spider climbs up 5 metres and slips down by 3 meters in a single step, it covers ( U - D ) m in each step and 96 m in 48 steps, but in the 49th step it climbs up 5 m and reaches out of the well and it will not slip down and the step is counted as one step.

Input:
The first line will contain an integer T (number of test cases). Each test case will contain 3 integers ’H’ height of the well, next ’U’ metres climbs up in each step, and the last ’D’ metres slips down in each step.

Output:
The number of steps 'N' required to get out of the well.

Constraints:
1 < = T < = 1000
50 < = H < = 1000
1  < = D < U < = 50

Example:
 Input:
2
200 50 1
500 20 15

Output:
5
98

Explanation:
Length of well = 200
Climbs up to = 50 m at each step
Slips down by = 1m at each step
Step 1 : Climbed up : 50 m
            Slipped down by : 1m
            Distance covered : 49 m
Step 2 : Climed up : 50 m ; reached at 99th m
             Slipped down by : 1m
             Total distance covered : 98m
Step 3 : Climed up : 50 m ; reached at 148th m
             Slipped down by : 1m
             Total distance covered : 147 m
Step 4 : Climed up : 50 m ; reached at 197th m
             Slipped down by : 1m
             Total distance covered : 196m
Step 5 : Climed up : 50 m ; reached out of the well
             Slipped down by : No slipping as reached 200th m
             Total distance covered : 200
"""


def the_spider_steps(h, u, d):
    return (h - d) // (u - d) + 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        h, u, d = [int(i) for i in input().split()][0:3]
        print(the_spider_steps(h, u, d))
