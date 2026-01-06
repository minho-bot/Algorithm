import sys, heapq

def main():
    N = int(sys.stdin.readline())
    gas_stations = [[0]*2 for _ in range(N)]
    # gas_stations 거리, 연료의 양
    for i in range(N):
        gas_stations[i] = list(map(int, sys.stdin.readline().split()))
    L, P = map(int, sys.stdin.readline().split())

    hq = []
    answer = 0
    now_position = P
    station_index = 0

    gas_stations.sort(key=lambda x: x[0])

    while now_position < L:    # 도착할 때 까지 반복
        for i in range(station_index, N):   # 주유소 순회
            station = gas_stations[i]
            # 도착 가능하면 힙큐에 넣기
            if station[0] <= now_position:
                heapq.heappush(hq, -station[1])
                station_index += 1
            else:
                break
        if hq:  # 남은 주유소 중 가장 기름 많은 곳에서 멈추기
            now_position -= heapq.heappop(hq)
            # print(f'now: {now_position}')
            answer += 1
        else:   # 모든 주유소를 방문해도 기름이 모잘라서 도착하지 못함
            answer = -1
            break
    
    print(answer)


main()

