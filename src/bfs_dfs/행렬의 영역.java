// nhn 모의 시험
/*
모든 원소가 '0' 또는 '1'인 행렬이 있습니다.
'1'로 표시된 원소는 영역을 나타내며, 상하좌우로 인접한 원소가 '1'이면 같은 영역입니다.

영역의 크기는 '1'로 표시된 원소의 개수로 정의합니다. 

주어진 행렬에서 영역의 개수와 각 영역의 크기를 출력하세요.

[입출력]
입력
6             // 행렬의 크기
0 1 1 0 0 0   // 6 * 6 사이즈의 행렬
0 1 1 0 1 1
0 0 0 0 1 1
0 0 0 0 1 1
1 1 0 0 1 0
1 1 1 0 0 0

입력값의 범위
1 <= 행렬의 크기 <= 10
행렬의 값은 공백으로 구분하여, 0과 1만 주어짐
solution 함수 파라미터
입력 데이터를 처리해서 solution 함수를 호출합니다. solution 함수를 완성해서 문제를 해결하세요.
solution(int sizeOfMatrix, int **matrix) 

sizeOfMatrix: 행렬의 크기
matrix: 행렬

출력
첫 번째 행은 영역의 개수를 출력합니다.
두 번째 행은 각 영역의 크기를 공백으로 구분하여 오름차순으로 출력합니다.
한 행의 끝은 불필요한 공백 없이 개행 문자(newline, \n)로 끝나야 합니다.

영역이 존재하지 않을 경우, 영역의 개수만 0으로 출력합니다.
[입출력 예시]
입력
6             // 행렬의 크기
0 1 1 0 0 0   // 6 * 6 사이즈의 행렬
0 1 1 0 1 1
0 0 0 0 1 1
0 0 0 0 1 1
1 1 0 0 1 0
1 1 1 0 0 0

출력
3          // 영역의 개수
4 5 7      // 각 영역의 크기

설명

영역은 3개이며, 각 영역의 크기는 4, 5, 7입니다.
*/
package bfs_dfs;

import java.util.*;
import java.util.stream.Collectors;

class Main {
	private static void solution(int sizeOfMatrix, int[][] matrix) {
		Deque<int[]> q = new ArrayDeque<>();
		boolean[][] visit = new boolean[sizeOfMatrix + 2][sizeOfMatrix + 2];
		int[][] newMatrix = new int[sizeOfMatrix + 2][sizeOfMatrix + 2];
		List<Integer> areaSizes = new LinkedList<>();
		final int[][] nexts = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
		for (int y = 0; y < sizeOfMatrix; y++) {
			for (int x = 0; x < sizeOfMatrix; x++) {
				newMatrix[y + 1][x + 1] = matrix[y][x];
			}
		}
		matrix = newMatrix;
		int areaCount = 0;
		for (int j = 0; j < sizeOfMatrix; j++) {
			for (int i = 0; i < sizeOfMatrix; i++) {
				if(visit[j+1][i+1] || matrix[j+1][i+1]==0){
					continue;
				}
				q.add(new int[]{j+1, i+1});
				areaCount+=1;
				int areaSize = 0;
				while (!q.isEmpty()) {
					int[] pop = q.pop();
					int y = pop[0], x = pop[1];
					if (visit[y][x] || matrix[y][x] == 0) {
						continue;
					}
					areaSize+=1;
					visit[y][x] = true;
					for (int[] next : nexts) {
						int dy = next[0];
						int dx = next[1];
						if (matrix[y + dy][x + dx] == 1 && !visit[y + dy][x + dx]) {
							q.add(new int[] { y + dy, x + dx });
						}
					}

				}
				if(areaSize>0) areaSizes.add(areaSize);
			}
			
		}
		System.out.println(areaCount);
		System.out.println(areaSizes.stream().sorted().map(s->Integer.toString(s)).collect(Collectors.joining(" ")));
	}

	private static class InputData {
		int sizeOfMatrix;
		int[][] matrix;
	}

	private static InputData processStdin() {
		InputData inputData = new InputData();

		try (Scanner scanner = new Scanner(System.in)) {
			inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

			inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
			for (int i = 0; i < inputData.sizeOfMatrix; i++) {
				String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
				for (int j = 0; j < inputData.sizeOfMatrix; j++) {
					inputData.matrix[i][j] = Integer.parseInt(buf[j]);
				}
			}
		} catch (Exception e) {
			throw e;
		}

		return inputData;
	}

	public static void main(String[] args) throws Exception {
		InputData inputData = processStdin();

		solution(inputData.sizeOfMatrix, inputData.matrix);
	}
}