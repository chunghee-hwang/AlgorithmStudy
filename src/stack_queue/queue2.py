# https://www.acmicpc.net/problem/18258
import sys
from collections import deque


def read_line():
    return sys.stdin.readline()


def read_command():
    return read_line().split()


if __name__ == '__main__':
    n = int(read_line())
    q = deque()
    output = []
    for i in range(n):
        commands = read_command()
        if len(commands) == 2:
            command, x = commands
        else:
            command = commands[0]

        if command == 'push':
            q.append(x)
        elif command == 'pop':
            if not q:
                output.append('-1')
            else:
                output.append(q.popleft())
        elif command == 'size':
            output.append(str(len(q)))
        elif command == 'empty':
            if q:
                output.append('0')
            else:
                output.append('1')
        elif command == 'front':
            if not q:
                output.append('-1')
            else:
                output.append(q[0])
        else: # back
            if not q:
                output.append('-1')
            else:
                output.append(q[-1])

    print('\n'.join(output))


