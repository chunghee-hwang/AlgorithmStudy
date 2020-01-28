package coding_test.쏘카;

import java.util.Arrays;
import java.util.LinkedList;

public class Solution1 {
    public static int[]solution(int[][]paths){
        int[] answer;
        int idx = 0;
        int len= paths.length;
        int[] fakeAfter = {-1,-1};
        LinkedList<Integer> list = new LinkedList<>();
        Arrays.sort(paths, (o1, o2) ->{
            if(o1[0]>o1[1] && o2[0]> o1[1]){
                return o2[0]-o1[0];
            }
            return o1[0]-o2[0];
        });
        for(int i = 0; i < len; i++){
            int[] cur = paths[i];
            int[]after = i!= len-1?paths[i+1]:fakeAfter;
            if(cur[1] == after[0]){
                after[0] = cur[0];
            }
            else{
                list.add(cur[0]);
                list.add(cur[1]);
            }
        }
        answer = new int[list.size()];
        for(Integer l : list){
            answer[idx++] = l;
        }
        return answer;
    }
    public static void main(String[] args) {
        int[][] paths = {{1,2},{2,3},{3,4},{8,7},{7,6}};
        System.out.println(Arrays.toString(solution(paths)));
        paths = new int[][]{{1, 2}, {4, 5}, {10, 9}, {3, 4}};
        System.out.println(Arrays.toString(solution(paths)));
    }
}
