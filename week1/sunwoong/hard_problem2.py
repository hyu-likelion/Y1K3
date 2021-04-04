caseNum = int(input())
for i in range(0, caseNum):
    students = list(map(int,input().split()))
    average = (sum(students)-students[0]) / students[0]
    
    over = 0
    for j in range(1, students[0]+1):
        if students[j] > average:
            over += 1
    
    print("%.3f%%" % (over / students[0] * 100))
    