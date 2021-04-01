word = str(input()).upper()

frequency_list = []

for i in set(word):
    num = word.count(i)
    frequency_list.append([i, num])

frequency_list.sort(key = lambda x:x[1], reverse = 1)

if len(frequency_list) > 1 and frequency_list[0][1] == frequency_list[1][1]:
    print('?')
else:
    print(frequency_list[0][0])
