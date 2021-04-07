from bwsi_grader.python.palindrome import grader

def student_func(x):
    x=x.upper()    
    x=x.replace(" ","")
    l=len(x)
    if(l==0):
        return True
    if x[0]==x[l-1]:
        x=x[1:l-1]
        return student_func(x)
    else:
        return False
grader(student_func)