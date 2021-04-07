# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

from bwsi_grader.python.three_five import grader


def student_func(x):
    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    if x%3 == 0 and x%5 ==0:
        return "threefive"
    elif x%3 == 0:
        return "three"
    elif x%5 == 0:
        return "five"
    else:
        return x


# Execute this cell to grade your work
grader(student_func)
