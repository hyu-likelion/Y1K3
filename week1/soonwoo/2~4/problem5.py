def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a=phone_book[i]
        b=phone_book[i+1]
        if len(a)>=len(b):
            continue
        chk=1
        for i in range(len(a)):
            if a[i]!=b[i]:
                chk=0
                break
        if chk==1:
            answer=False
            break
    return answer
