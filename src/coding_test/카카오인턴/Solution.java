package coding_test.카카오인턴;

import java.util.Stack;
//결과 :정확성 100% 효율성 검사 없음
public class Solution {
    public static int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();
        int n = board[0].length;
        int[] heights = new int[n];
        for(int y = 0; y < n; y++){
            for(int x = 0; x < n; x++){
                if(board[y][x] != 0 && heights[x] == 0)
                {
                    heights[x] = y+1;
                }
            }
        }
        int cnt = 0;
        for (int move : moves) {
            if(heights[move-1] > n) continue;
            int k = board[heights[move - 1] - 1][move - 1];
            heights[move - 1]++;
            if (k == 0) continue;
            if (stack.isEmpty() || stack.peek() != k)
                stack.push(k);
            else {
                stack.pop();
                cnt+=2;
            }

        }
        return cnt;
    }

    public static void main(String[] args) {
        int[][] board = {
                {0, 0, 0, 0, 0},
                {0, 0, 1, 0, 3},
                {0, 2, 5, 0, 1},
                {4, 2, 4, 4, 2},
                {3, 5, 1, 3, 1}};
        int[] moves = {1, 5, 3, 5, 1, 2, 1, 4};
        System.out.println(solution(board, moves));
    }
}
