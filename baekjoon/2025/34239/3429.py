# -1 2 -4 -2 3
# 홀수 시작
# -1 -2 -4 2 3
# 짝수 시작
# (-1) 2 4 -2 -3
# 이렇게 다 만들어놓은 다음 젤 앞 부터 누적으로 더함
# 더했는데 음수면 쓸 필요 없음.. sum 을 0으로 초기화함
# 이렇게 해서 끝까지 탐색해서 가장 큰 수 구하면 됨
# 어디서 멈추는지는 상관이 없으나, 시작 위치는 홀수/짝수 정해져있음
# 음수인지 체크는 어디서든 해도 되지만 짝수시작인데 짝수에서 음수면 홀수에서 시작할 수 없음


import sys
def main():
    N = int(sys.stdin.readline())
    # print(f'N: {N}')
    num_list = list(map(int, sys.stdin.readline().split()))

    # print(f'num_list: {num_list}')

    odd_list = [0] * N
    even_list = [0] * N

    for i in range(0, N):
        if i == 0:
            odd_list[i], even_list[i] = num_list[i], num_list[i]
            continue
        if i%2 == 1:
            odd_list[i], even_list[i] = -num_list[i], num_list[i]
        else:
            odd_list[i], even_list[i] = num_list[i], -num_list[i]
            
    # print(f'odd_list: {odd_list}')
    # print(f'even_list: {even_list}')

    answer = get_odd_max(odd_list, N)
    if N > 1:
        answer = max(get_even_max(even_list, N), answer)
    return answer

def get_odd_max(odd_list:list, N:int):
    odd_sum = 0
    odd_max = odd_list[0]
    for i in range(0, N):
        if i%2 == 0 and odd_sum < 0:
            odd_sum = 0
        odd_sum += odd_list[i]
        odd_max = max(odd_max, odd_sum)
        # print(f'odd_max: {odd_max}')

    # print(f'odd_max: {odd_max}')
    return odd_max

# 여기서부터는 N이 1보다 커야 가능
def get_even_max(even_list:list, N:int):
    even_sum = 0
    even_max = even_list[1]
    for i in range(1, N):
        if i%2 == 1 and even_sum < 0:
            even_sum = 0
        even_sum += even_list[i]
        even_max = max(even_max, even_sum)
        # print(f'even_max: {even_max}')

    # print(f'even_max: {even_max}')
    return even_max

answer = main()
print(f'{answer}')
