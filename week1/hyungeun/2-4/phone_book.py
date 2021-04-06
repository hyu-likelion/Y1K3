def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])
        for j in range(length):
            if phone_book[i + 1][:length] == phone_book[i]:
                return False
        
    return answer
    