# https://www.acmicpc.net/problem/1966
import sys
from collections import deque
answers = []
def simulate_print(target, documents):
    q = deque([(pri, idx) for idx, pri in enumerate(documents)])
    print_rank = 0
    while q:
        doc = q.popleft()
        pri, idx = doc
        if not q:
            max_pri = 0
        else:
            max_pri = max(q)[0]
        if pri < max_pri:
            q.append(doc)
        else:
            print_rank+=1
            if idx == target:
                answers.append(str(print_rank))
                break

tn = int(sys.stdin.readline())
for _ in range(tn):
    n, target = map(int, sys.stdin.readline().split(' '))
    documents = [*map(int, sys.stdin.readline().split(' '))]
    simulate_print(target, documents)
print('\n'.join(answers))
