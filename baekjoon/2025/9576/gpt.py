import sys
input = sys.stdin.readline

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    req = [tuple(map(int, input().split())) for _ in range(M)]
    # 오른쪽 끝 b 기준 오름차순
    req.sort(key=lambda x: x[1])

    # parent[x] = x 이상에서 "가장 먼저 남은" 책 번호를 가리킴
    parent = list(range(N + 2))  # 1..N, N+1은 가드

    ans = 0
    for a, b in req:
        x = find(a, parent)      # a 이상에서 남은 첫 책
        if x <= b:               # 구간 [a,b] 안이면 배정 가능
            ans += 1
            parent[x] = find(x + 1, parent)  # x는 사용했으니 다음으로 연결
    print(ans)