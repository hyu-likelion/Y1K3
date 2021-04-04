def solution(phone_book):
    answer = True

    #  list 정렬
    phone_book.sort()

    # 바로 뒤와 비교
    # 오름차순 정렬되어 있으므로 어차피 바로 뒤에 것에 포함되어 있지 않으면 가망이 없다.
    for i in range(0, len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i]) == 0:
            answer = False
            break

    return answer


answer = solution(["119", "97674223", "1195524421"])
print(answer)