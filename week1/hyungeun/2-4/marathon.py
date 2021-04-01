def solution(participant, completion):
    
    answer = ""
    temp1 = 0
    temp2 = 0
    participant = [x.encode() for x in participant]
    completion = [x.encode() for x in completion]
    for i in participant:
        temp1 += int.from_bytes(i, byteorder='big')
    for j in completion:
        temp2 += int.from_bytes(j, byteorder='big')

    diff = temp1 - temp2

    for i in participant:
        temp = int.from_bytes(i, byteorder='big')
        if diff == temp:
            answer = i.decode()
    
    
    return answer
#string 연산으로 푸는 것보다 16진수로 encoding한 다음 숫자를 통하여 연산 후 decoding 하면 효율성이 
#좋을 것 같아 시도해봄.