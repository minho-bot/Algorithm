import sys

def main():
    K, N = map(int, sys.stdin.readline().split())
    num = []
    

    for _ in range(K):
        str_n = sys.stdin.readline().rstrip()
        int_n = int(str_n)
        num.append((str_n, int_n))

    num.sort(key=make_10, reverse=True)
    # print(num)

    long_ind = 0
    long_len = 0

    for i in range(K-1, -1, -1):
        n = num[i][0]
        l = len(n)
        # print(f'l: {l}')
        if l >= long_len:
            long_len = l
            long_ind = i

    ans = []

    for i in range(K):
        ans.append(num[i][0])

        if i == long_ind:
            # print(f'long_ind: {long_ind}')
            for _ in range(N-K):
                ans.append(num[i][0])
    
    print(''.join(ans))


def make_10(num: tuple):
    n = num[0]
    i = 0
    ind = 0
    l = len(n)
    li = []
    while i < 10:
        li.append(n[ind])
        i += 1
        ind += 1
        ind %= l
    return int(''.join(li))





    


main()