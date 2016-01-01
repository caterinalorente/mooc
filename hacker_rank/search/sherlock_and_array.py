"""
https://www.hackerrank.com/challenges/sherlock-and-array

Watson gives Sherlock an array A of length N.
Then he asks him to determine if there exists an element in the array such that the sum of the elements on its left
is equal to the sum of the elements on its right.
If there are no elements to the left/right, then the sum is considered to be zero.

Formally, find an i, such that, A1+A2...Ai-1 =Ai+1+Ai+2...AN.

-- Input Format --
The first line contains T, the number of test cases.
For each test case, the first line contains N, the number of elements in the array A.

The second line for each test case contains N space-separated integers, denoting the array A.

-- Output Format --
For each test case print YES if there exists an element in the array, such that the sum of the elements on its left
is equal to the sum of the elements on its right; otherwise print NO.

-- Constraints --
1 <= T <= 10
1 <= N <= 10exp5
1 <= Ai<= 2×104
1 <= i <= N

Sample Input
2
3
1 2 3
4
1 2 3 3

Sample Output
NO
YES
"""

import sys

def extract_array_from_data(data_line):

    array_position = data_line + 1
    array_with_spaces = data.split("\n")[array_position]
    array_of_strings = list(filter((lambda x: x.isdigit()), array_with_spaces))
    return list(map((lambda x: int(x)), array_of_strings))


def sherlock_and_array(data):

    number_of_tests = int(data.split("\n")[0])
    data_line = 1

    for i in range(0, number_of_tests):
        array_length = int(data.split("\n")[data_line])
        array = extract_array_from_data(data_line)

        if array_length > 2:
            for i in range(1, array_length):
                if sum(array[:i]) == sum(array[i+1:]):
                    print("YES")
                    quit()
            print("NO")
        else:
            if array_length == 1:
                print("YES")
            elif array_length == 2:
                if array[1] == 0:
                    print("YES")
                else:
                    print("NO")

        data_line += 2

data = "2\n3\n1 2 3\n4\n1 2 3 3"
# data = sys.stdin.read()
sherlock_and_array(data)