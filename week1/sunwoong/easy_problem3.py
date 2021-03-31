num = input()
total = input().split()
total = list(map(int, total))

print(str(min(total)) + ' ' + str(max(total)))