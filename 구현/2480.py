# 주사위 세개 
a = list(map(int, input().split()))

print(a)

if a[0] == a[1] == a[2]:
    ans = 10000 + a[0]*1000
elif a[0] == a[1] or a[0] == a[2]:
    ans = 1000 + a[0]*100
elif a[1] == a[2]:
    ans = 1000 + a[1]*100
else:
    ans = max(a) * 100

print(ans)