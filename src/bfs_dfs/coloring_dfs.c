#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
char d[10][10];
int n, m;
int visit[10][10];

void dfs(int x, int y)
{
	if (x < 0 || y < 0 || x == 10 || y == 10) {
		return;
	}
	if (visit[x][y] == 1) {
		return;
	}

	visit[x][y] = 1;

	if (d[x][y] == '*') {
		return;
	}
	if (d[x][y] == '_') {
		d[x][y] = '*';
	}

	dfs(x - 1, y);
	dfs(x, y - 1);
	dfs(x + 1, y);
	dfs(x, y + 1);
}

void solve()
{
	dfs(n, m);
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