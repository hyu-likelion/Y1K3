# Execute this cell to grade your work
from bwsi_grader.python.palindrome import grader


# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

def student_func(x):
    # `x` is a string
    # this function should return either `True` or `False`
    
    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    x = x.replace(" ", "")
    x = x.lower()
    words = list(x)
    length = len(x)

    for i in range(0, int(length/2)):
        if words[i] != words[length-i-1]:
            return False
    return True


grader(student_func)
