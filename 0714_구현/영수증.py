X = int(input())
N = int(input())
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += a*b

if X == ans:
    print("Yes")
else:
    print("No")
