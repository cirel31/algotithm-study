from _collections import deque

now, total = map(int, input().split())

currentPage = None
backwardStack = deque()
forwardStack = deque()

for _ in range(total):
    order = input().split()
    cmd = order[0]

    if cmd == 'B' and backwardStack:
        forwardStack.appendleft(currentPage)
        currentPage = backwardStack.pop()
    elif cmd == 'F' and forwardStack:
        backwardStack.append(currentPage)
        currentPage = forwardStack.popleft()
    elif cmd == 'A':
        if currentPage is not None:
            backwardStack.append(currentPage)
        forwardStack.clear()
        currentPage = int(order[1])
    elif cmd == 'C':
        compressed_backward = deque()
        last_page = None
        while backwardStack:
            page = backwardStack.pop()
            if page != last_page:
                compressed_backward.appendleft(page)
                last_page = page
        backwardStack = compressed_backward

print(currentPage if currentPage is not None else -1)
print(' '.join(map(str, reversed(backwardStack))) if backwardStack else -1)
print(' '.join(map(str, forwardStack)) if forwardStack else -1)
