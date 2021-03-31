participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
temp1 = 0
temp2 = 0
participant = [x.encode() for x in participant]
completion = [x.encode() for x in completion]
for i in participant:
    temp1 += int.from_bytes(i, byteorder='big')
for j in completion:
    temp2 += int.from_bytes(j, byteorder='big')

print(participant)
diff = temp1 - temp2

for i in participant:
    temp = int.from_bytes(i, byteorder='big')
    if diff == temp:
        answer = i.decode()

print(answer)