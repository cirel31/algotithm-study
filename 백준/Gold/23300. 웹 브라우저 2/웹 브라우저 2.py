from _collections import deque

now, total = map(int, input().split())

currentPage = None  # 초기 현재 페이지 설정. None은 아직 아무 페이지에 접속하지 않은 상태
backwardStack = deque()  # 뒤로 가기 스택
forwardStack = deque()  # 앞으로 가기 스택

for _ in range(total):
    order = input().split()
    cmd = order[0]

    if cmd == 'B' and backwardStack:
        # 뒤로 가기: backwardStack에서 가장 최근 페이지를 꺼내 현재 페이지로 설정하고, 이전 현재 페이지를 forwardStack에 추가
        forwardStack.appendleft(currentPage)
        currentPage = backwardStack.pop()
    elif cmd == 'F' and forwardStack:
        # 앞으로 가기: forwardStack에서 가장 최근 페이지를 꺼내 현재 페이지로 설정하고, 이전 현재 페이지를 backwardStack에 추가
        backwardStack.append(currentPage)
        currentPage = forwardStack.popleft()
    elif cmd == 'A':
        # 웹 페이지 접속: 첫 번째 웹페이지 접속이 아닐 경우 현재 페이지를 backwardStack에 추가하고, forwardStack을 초기화 
        if currentPage is not None:
            backwardStack.append(currentPage)
        forwardStack.clear()
        currentPage = int(order[1])
    elif cmd == 'C':
        # 압축: backwardStack에서 연속된 중복 페이지를 제거
        compressed_backward = deque()
        last_page = None
        while backwardStack:
            page = backwardStack.pop()
            if page != last_page:
                compressed_backward.appendleft(page)
                last_page = page
        backwardStack = compressed_backward

print(currentPage if currentPage is not None else -1)  # 현재 페이지 출력
# backwardStack과 forwardStack의 내용을 역순으로 출력합니다. 스택이 비어있으면 -1을 출력
print(' '.join(map(str, reversed(backwardStack))) if backwardStack else -1)
print(' '.join(map(str, forwardStack)) if forwardStack else -1)
