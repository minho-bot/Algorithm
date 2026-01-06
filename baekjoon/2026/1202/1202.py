import sys, heapq

def main():
    N, K = map(int, sys.stdin.readline().split())
    # print(f'N: {N}, K: {K}')
    
    # 보석 무게, 가격 저장
    jewels = [[0] * 2 for _ in range(0, N)]
    for i in range(0, N):
        jewels[i][0], jewels[i][1] = map(int, sys.stdin.readline().split())
    # 가방 무게, 방문 저장
    bags = [0] * K
    for i in range(0, K):
        bags[i] = int(sys.stdin.readline())
    # print(f'jewels: {jewels}')
    # print(f'bags: {bags}')
    
    jewels.sort(key=lambda x: x[0])
    bags.sort()

    # print(f'jewels: {jewels}')
    # print(f'bags: {bags}')

    hq = []
    answer = 0
    j_index = 0

    for bag in bags:
        # print(f'bag: {bag}')
        for i in range(j_index, N):
            # print(f'j_index: {j_index}')
            jewel = jewels[i]
            if jewel[0] <= bag:
                heapq.heappush(hq, -jewel[1])
                j_index += 1
            else:
                break
        if len(hq) > 0:
            target = heapq.heappop(hq)
            answer += target
        # print(answer)
    
    print(-answer)
    


main()