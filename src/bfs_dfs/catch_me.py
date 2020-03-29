# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/
import sys
from collections import deque


# 브라운이 코니를 잡았다는 뜻이 코니와 위치가 같거나, 앞질러도 잡았다고 판단
def catch_conny(cony_position, brown_position):
    time = 0
    visit = [[False for _ in range(2)] for _ in range(200001)]
    queue = deque()
    queue.append((brown_position, 0))
    while True:
        cony_position += time
        if cony_position > 200000:
            return -1
        if visit[cony_position][time % 2]:
            return time
        queue_size = len(queue)
        for _ in range(queue_size):
            queue_front = queue[0]
            current_position = queue_front[0]
            new_time = (queue_front[1] + 1) % 2

            queue.popleft()
            new_position = current_position - 1
            if new_position >= 0 and not visit[new_position][new_time]:
                visit[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and not visit[new_position][new_time]:
                visit[new_position][new_time] = True
                queue.append((new_position, new_time))
            new_position = current_position * 2
            if new_position < 200001 and not visit[new_position][new_time]:
                visit[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


if __name__ == '__main__':
    print('time:', catch_conny(11, 2))
    print('time:', catch_conny(6, 3))
