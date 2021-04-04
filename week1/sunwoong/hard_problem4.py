def solution(participant, completion):
    participant.sort()
    completion.sort()

    for num in range(0, len(completion)):
        if participant[num] != completion[num]:
            return participant[num]
    
    return participant[len(participant)-1]

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])