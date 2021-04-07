from bwsi_grader.python.three_five import grader

def student_func(x):
    answer=""
    if x%3==0:
        answer=answer+"three"
    if x%5==0:
        answer=answer+"five"
    if answer=="":
        return x
    return answer
grader(student_func) 