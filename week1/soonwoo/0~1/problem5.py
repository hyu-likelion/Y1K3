def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    chk=0
    for i in range(len(completion)):
        if completion[i]!=participant[i]:
            chk=1
            answer=participant[i]
            break
    if chk==0:
        answer=participant[len(participant)-1]
    return answer
