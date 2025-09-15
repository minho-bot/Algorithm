# 우선 순위??
# 가장 인기가 적은 책 부터 나눠주는데, 범위가 가장 좁은사람에게 주면?
# 책과 사람을 2차원 배열로 만든다
# 책 수 N, 사람 수 M

import sys

def test_case(N:int, M:int, arr:list):
    answer = 0
    # print_arr(N, M, arr)
    while(True):
        book = get_min_popular_book_num(arr, N)
        # print(f'book: {book}')
        if book >= 1:
            # 책이 아직 남았음
            person = get_most_narrow_person(book, arr, M)
            # print(f'person: {person}')
            arr[0][book] = 0
            for i in range(1, M+1):
                if arr[i][book] == 1:
                    arr[i][book] = 0
                    arr[i][0] -= 1

            arr[person][0] = 0
            for i in range(1, N+1):
                if arr[person][i] == 1:
                    arr[person][i] = 0
                    arr[0][i] -= 1
            answer += 1
            # print_arr(N, M, arr)
            # break
        else:
            # 이제 모든 책을 나눠주었음
            break
    return answer


def init_arr(N:int, M:int, arr:list):
    for i in range(1, M+1):
        start, end = map(int, sys.stdin.readline().split())
        for j in range(start, end+1):
            arr[i][j] = 1
            arr[i][0] += 1  # 이 사람이 원하는 책의 개수 합계
            arr[0][j] += 1  # 이 책을 원하는 사람의 수 합계

def get_most_narrow_person(book: int, arr: list, M: int):
    min_index, min_val = 0, 1001
    for i in range(1, M+1):
        # 이 책을 원하지 않는 사람은 건너띔
        if arr[i][book] < 1:
            continue
        if arr[i][0] < min_val:
            min_val = arr[i][0]
            min_index = i
    return min_index


def get_min_popular_book_num(arr: list, N: int):
    min_index, min_val = 0, 1001
    for i in range(1, N+1):
        # 아무도 원하지 않는 책은 건너띔
        if arr[0][i] < 1:
            continue
        if arr[0][i] < min_val:
            min_val = arr[0][i]
            min_index = i
            # print(f'max_val: {max_val}, max_index: {max_index}')
    return min_index

def print_arr(N: int, M: int, arr: list):
    print("=====start=====")
    for i in range(0, M+1):
        for j in range(0, N+1):
            print(f'{arr[i][j]} ', end='')
        print()
    print("======end======")


def main():
    tc_size = int(sys.stdin.readline())
    N, M = 0, 0
    # 미리 1001 * 1001 의 배열을 만들어 놓고 인덱스 0 에서는 합계를 관리한다. 거의 엑셀임
    arr = [([0] * 1001) for _ in range(0, 1001)]
    for i in range(0, tc_size):
        N, M = map(int, sys.stdin.readline().split())
        # print(f'N: {N}, M:{M}')
        # 배열 입력값으로 초기화
        init_arr(N, M, arr)
        # 테스트 케이스 실행
        answer = test_case(N, M, arr)
        print(f'{answer}')
        # 배열 0으로 초기화

main()