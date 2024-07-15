import sys
n = int(sys.stdin.readline())

n
for i in range(n):
    s_input = input()
    ans = s_input[0]+ s_input[-1]
    print(ans)
