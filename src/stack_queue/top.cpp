// https://programmers.co.kr/learn/courses/30/lessons/42588?language=cpp
#include <vector>
#include <stack>
using namespace std;
struct TOWER{
	int height;
	TOWER* left;
};
vector<int> solution(vector<int> heights) {
	stack<TOWER> s;
	TOWER *lastTower = nullptr;
	vector<int> answer(heights.size(), 0);
	for (int i = 0; i < heights.size(); i++) {
		TOWER tower = TOWER{ heights[i], lastTower };
		s.push(tower);
		lastTower = new TOWER(tower);
	}
	int send_pos = s.size()-1;
	while (!s.empty()) {
		TOWER curTower = s.top();
		TOWER *ptr = &curTower;
		int receive_pos = send_pos-1;
		while (ptr->left != nullptr){
			if (curTower.height < ptr->left->height)
			{
				answer[send_pos] = (receive_pos+1);
				break;
			}
            receive_pos--;
            ptr = ptr->left;
		} 
		s.pop();
		send_pos--;
	}
	return answer;
}