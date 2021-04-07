def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])
        for j in range(length):
            if phone_book[i + 1][:length] == phone_book[i]:
                return False
        
    return answer
<<<<<<< HEAD
    
=======
   
>>>>>>> 7f4331be2834c1cff9522ec6b03301c963497e24
