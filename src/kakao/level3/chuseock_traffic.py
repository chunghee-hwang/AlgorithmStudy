# 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676
# 참고 사이트: https://medium.com/@dltkddud4403/2018-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B8%94%EB%9D%BC%EC%9D%B8%EB%93%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD-450067ce84a8
def time_to_seconds(time):
    h, m, s_ss = time.split(':')
    h = int(h); m = int(m); s_ss = float(s_ss)
    return h*3600 + m*60 + s_ss
def get_log_info(log):
    date, end_time, interval = log.split(' ')
    end_time = time_to_seconds(end_time)
    interval = float(interval[:-1])
    start_time = end_time - interval + 0.001
    return (start_time, end_time)

def lt(v1, v2):
    return v1-v2 <= 0.001

def solution(lines):
    answer = 0
    log_infos = [get_log_info(line) for line in lines]
    for log_info in log_infos:
        process_amount = 0
        check_start_time = log_info[1]
        check_end_time = check_start_time+0.999
        for start_time, end_time in log_infos:
            if lt(start_time,check_end_time) and lt(check_start_time, end_time):
                process_amount+=1
        answer = max(answer, process_amount)
    return answer