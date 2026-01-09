import sys

def main():
    T = int(sys.stdin.readline())
    num = []
    max_num = 0
    for _ in range(T):
        n = int(sys.stdin.readline())
        num.append(n)
        max_num = max(max_num, n)

    li = [1] * (max_num+1)
    dp(max_num, li)
    # print(li)
    for n in num:
        print(li[n])


def dp(n: int, li: list):
    # 2 채우기
    for i in range(2, n+1):
        li[i] += li[i-2]
    for i in range(3, n+1):
        li[i] += li[i-3]
    return 0






    



main()

# 1

# 1+1
# 2

# 1+1+1
# 1+2
# 3

# 1+1+1+1
# 1+1+2
# 2+2
# 1+3

# 1+1+1+1+1
# 1+1+1+2
# 1+2+2
# 1+1+3
# 2+3

# 1+1+1+1+1+1