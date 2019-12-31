package coding_test.programmers_test2;

import java.util.Arrays;

public class Test2 {
    public static int[] solution(int[] heights) {
        int len = heights.length;
        int[] answer = new int[len];
        for (int i = 0; i < len; i++) {
            int cur = heights[i];
            for (int k = i-1; k >= 0; k--) {
                if (cur < heights[k]) {
                    answer[i] = k + 1;
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int []heights = {6,9,5,7,4};
        System.out.println(Arrays.toString(solution(heights)));
    }
}
