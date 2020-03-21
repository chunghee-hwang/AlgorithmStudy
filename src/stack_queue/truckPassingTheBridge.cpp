// https://programmers.co.kr/learn/courses/30/lessons/42583?language=cpp
#include <vector>
#include <deque>
using namespace std;
struct TRUCK {
	int weight;
	int *cross_dist;
};
int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int curWeight = weight, curLength = bridge_length, time = 0;
	deque<TRUCK> waitQ, crossQ, finishQ;
	for (int tw : truck_weights)
		waitQ.push_back(TRUCK{ tw, new int(0) });
	while (finishQ.size() != truck_weights.size()) {
		time++;
		deque<TRUCK>::iterator it = crossQ.begin();
		if (it != crossQ.end()) {
			do {
				(*(it->cross_dist))++;
				it++;
			} while (it != crossQ.end());
		}
		if (!crossQ.empty()) {
			TRUCK c_truck = crossQ.front();
			if (*c_truck.cross_dist >= bridge_length) {
				crossQ.pop_front();
				curWeight += c_truck.weight;
				finishQ.push_back(c_truck);
				curLength += 1;
			}
		}
		if (!waitQ.empty()) {
			TRUCK w_truck = waitQ.front();
			if (curWeight - w_truck.weight >= 0 && curLength - 1 >= 0) {
				curWeight -= w_truck.weight;
				curLength -= 1;
				waitQ.pop_front();
				crossQ.push_back(w_truck);
			}
		}
	}
	for (TRUCK truck : finishQ)
		delete(truck.cross_dist);
	return time;
}