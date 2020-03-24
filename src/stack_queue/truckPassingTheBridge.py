# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
from collections import deque


class Truck:
    def __init__(self, weight):
        self.weight = weight
        self.travelDistance = 0

    def move(self):
        self.travelDistance += 1

    def __str__(self):
        return 'Truck: weight: {}, travelDistance: {}'.format(self.weight, self.travelDistance)


def moveAllTrucksInBridge(bridge):
    for truck in bridge:
        truck.move()


def dumpInfo(seconds, curWeight, bridge, trucks):
    print('\nseconds:', seconds, '\ncurWeight:', curWeight, '\nbridge: ')
    for truck in bridge: print(truck)
    print('trucks: ')
    for truck in trucks: print(truck)


def solution(bridge_length, weight, truck_weights):
    trucks = deque()
    for truck_weight in truck_weights: trucks.append(Truck(truck_weight))
    bridge = deque()
    seconds = 0
    curweight = 0
    while True:
        # dumpInfo(seconds, curWeight, bridge, trucks)
        moveAllTrucksInBridge(bridge)
        if bridge and bridge[0].travelDistance > bridge_length:
            truck = bridge.popleft()
            curweight -= truck.weight
        if trucks and (trucks[0].weight + curweight <= weight):
            truck = trucks.popleft()
            curweight += truck.weight
            truck.move()
            bridge.append(truck)
        seconds += 1
        if not bridge:
            break
    return seconds


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
