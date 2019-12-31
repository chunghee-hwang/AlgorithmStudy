#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)

char d[10][10]; // 그림
int n, m; // x, y 입력값
int visit[10][10]; // 방문 좌표

int front = 0; // 큐의 프론트
int back = 0; // 큐의 백

// 좌표 구조체
typedef struct coord {
	int x, y;
}coord;

#define QUEUE_SIZE 100

// 색칠할 예정인 좌표들을 담을 큐
coord q[QUEUE_SIZE];

// 큐가 비어있는 지 참거짓 반환하는 함수
int isQueueEmpty() {
	return front == back;
}

// 큐에 좌표를 추가하는 함수
void addToQueue(coord c) {
	q[back] = c;
	back = (back + 1) % QUEUE_SIZE;
}

// 큐에서 좌표를 하나 꺼내는 함수
coord removeFromQueue() {
	coord elem = q[front];
	front = (front + 1) % QUEUE_SIZE;
	return elem;
}

// 좌표 c가 색칠가능한 지 참거짓 반환하는 함수
int isColorable(coord c) {
	int x = c.x; 
	int y = c.y;
	return (x >= 0 && y >= 0 && x <= 9 && y <= 9 && d[x][y] == '_');
}

void solve()
{
	int x = n;
	int y = m;
	
	coord c = { x,y }; //처음에 입력받은 좌표가

	if (isColorable(c)) { //색칠 가능하다면 
		addToQueue(c); //큐에 집어넣음
	}
	while (!isQueueEmpty()) //큐가 빌 때까지 반복
	{
		coord current = removeFromQueue(); //큐에서 좌표 하나를 꺼냄
		int x = current.x;
		int y = current.y;
		if (visit[x][y]) continue; //이미 방문한 좌표라면 다음 좌표를 꺼내러 가기
		d[x][y] = '*'; //색칠
		visit[x][y] = 1; //방문 체크
		coord top = { x, y-1 }; 
		coord bot = { x, y+1 };
		coord left = { x-1, y };
		coord right = { x + 1, y };

		//현재 좌표 기준 (위,아래, 왼쪽, 오른쪽)에있는 좌표가 색칠 가능하다면 큐에 집어넣는다.
		if (isColorable(top)) addToQueue(top); 
		if (isColorable(bot)) addToQueue(bot);
		if (isColorable(left)) addToQueue(left);
		if (isColorable(right)) addToQueue(right);
	}
}

void input()
{
	int i, j;
	for (i = 0; i < 10; i++) {
		for (j = 0; j < 10; j++) {
			scanf("%1c", &d[j][i]);
		}
		scanf("\n");
	}
	scanf("%d %d", &n, &m);

}

void output()
{
	int i, j;
	for (i = 0; i < 10; i++) {
		for (j = 0; j < 10; j++) {
			printf("%c", d[j][i]);
		}
		printf("\n");
	}
}

main()
{
	input();
	solve();
	output();
	
}