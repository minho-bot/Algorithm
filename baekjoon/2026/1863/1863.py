import sys

def main():
    n = int(sys.stdin.readline())
    sky_line = []
    stack = []
    answer = 0
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        sky_line.append(y)
    
    top = 0
    for height in sky_line:
        # print(f'height: {height}')
        # print(f'top: {top}')
        # if stack:
        #     top = stack[-1]
        # else:
        #     top = 0

        if height > top:
            stack.append(height)
            answer += 1
            top = height
        elif height == top:
            pass
        else:
            stack.pop()
            top = stack[-1] if len(stack) > 0 else 0
            # print(f'this top: {top}')
            if height > top:
                stack.append(height)
                answer += 1
                top = height
            elif height == top:
                pass
            else:
                while stack and height < top:
                    stack.pop()
                    top = stack[-1] if len(stack) > 0 else 0
                if height == top:
                    pass
                elif height > top:
                    stack.append(height)
                    answer += 1
                    top = height
    print(answer)

main()
