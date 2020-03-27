import sys

stations = []


class Destination(tuple):
    def __lt__(self, other):
        if self[1] != other[1]:
            return self[1] < other[1]
        else:
            return self[0] < other[0]

    def __gt__(self, other):
        if self[1] != other[1]:
            return self[1] > other[1]
        else:
            return self[0] > other[0]


def read_line():
    return sys.stdin.readline()


def read_ints():
    return list(map(int, read_line().split()))


def find_rail_path(station, visited, r, sum_of_passengers, num_of_passengers):
    visited[station] = True
    sum_of_passengers += num_of_passengers[station]

    if station != 1:
        stations.append(Destination((station, sum_of_passengers)))

    connected_stations = r[station]

    for connected_station in connected_stations:
        if not visited[connected_station]:
            find_rail_path(connected_station, visited, r, sum_of_passengers, num_of_passengers)


if __name__ == '__main__':
    n = int(read_line())
    passengers = [0] + read_ints()
    rails = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        station1, station2 = read_ints()
        rails[station1].append(station2)
        rails[station2].append(station1)

    visit = [False for _ in range(n + 1)]
    find_rail_path(1, visit, rails, 0, passengers)
    num, sum_of_pass = max(stations)
    print(num, sum_of_pass)
