def solution(a, b, budget):
    case_count = 0
    max_buy_a_count = 23000 // a
    for buyACount in range(max_buy_a_count+1):

        if (budget - (a * buyACount)) % b == 0:
            print('a 구매: ', buyACount, 'b 구매: ', (budget - (a * buyACount)) // b)
            case_count += 1
    return case_count


if __name__ == '__main__':
    print(solution(3000, 5000, 23000))
