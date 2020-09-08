# 오픈 채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
from collections import defaultdict
def solution(records):
    answer = []
    history = []
    user_db = defaultdict(str)
    for record in records:
        commands = record.split(' ')
        if len(commands) > 2:
            operation, uid, nickname = commands
            if operation == 'Enter':
                history.append((uid, operation))
            user_db[uid] = nickname
        else:
            operation, uid = commands
            history.append((uid, operation))
    for uid, operation in history:
        if operation == 'Enter':
            suffix = "님이 들어왔습니다."
        else:
            suffix = "님이 나갔습니다."
        answer.append(user_db[uid]+suffix)
    return answer