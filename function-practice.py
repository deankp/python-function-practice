# Write a Python function called max_num()to find the maximum of three numbers.

from math import prod
from random import triangular
from tkinter.messagebox import RETRY


def max_num(a, b, c):
    return max([a, b, c])


print(max_num(7, 8, 9))
print(max_num(10, 20, 30))
print(max_num(69, 67, 68))

# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(list):
    # if list empty, return 0
    if len(list) == 0:
        return 0
    # items start with first element
    item = list[0]

    # go through list and multiply them together
    if len(list) > 1:
        for i in list[1:]:
            item = item * i
    return item


print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([15]))

# Write a Python function called rev_string() to reverse a string.


def rev_string(some_string):
    return some_string[::-1]


print(rev_string(""))
print(rev_string("bananna"))
print(rev_string("no se"))

# Write a Python function called num_within() to check whether a number falls in a given range.


def num_within(a, b, c):
    return a in range(b, c + 2)


print(num_within(4, 2, 2))
print(num_within(1, 2, 3))
print(num_within(10, 5, 12))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1], [1, 1]]


def pascal(n):
    # base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                # first number is 1
                if i == 0:
                    row.append(1)
                # intermediate numbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number - 1]
                               [i-1]+triangle[row_number - 1][i])
                # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1


        # print triangle
pascal(2)
pascal(5)
