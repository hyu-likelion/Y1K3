a = input()
a_i = int(a)
li = list(map(int, input().split()))
ans = li[0:a_i]
minimum = min(ans)
maximum = max(ans)

print(str(minimum) + " " + str(maximum))