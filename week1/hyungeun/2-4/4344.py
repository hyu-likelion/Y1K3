
def calculate_mean(arr):
    return sum(arr) / len(arr)

def calculate_ratio(arr, mean):
    over = 0
    for x in arr:
        if x > mean:
            over += 1
    
    return float(over / len(arr))

cases = int(input())
answers = []
for i in range(cases):
    members = list(map(int, input().split()))
    num = members[0]
    scores = members[1:num + 1]
    mean = calculate_mean(scores)
    ratio = calculate_ratio(scores, mean)
    answers.append(ratio * 100)

for i in answers:
    print("{:.3f}%".format(i))