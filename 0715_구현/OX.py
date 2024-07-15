import sys
n = int(sys.stdin.readline())

n
for i in range(n):
    test = input()
    ans = 0
    score = 0
    for i in range(len(test)):
        if test[i] == "O":
            score += 1
        elif test[i] == "X":
            score -= score
        ans += score
    print(ans)

