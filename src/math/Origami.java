package src.math;

import java.util.Arrays;

//https://programmers.co.kr/learn/courses/30/lessons/62049
//종이접기
public class Origami {
    //규칙 : ""는 접었을 때 새로 생긴 선을 말함
    // 0: 점선, 1: 실선
    // n:0 []
    // n:1 ["0"]
    // n:2 -> n:1에서 0 앞뒤로 0,1을 끼워넣는다
    // ["0" 0 "1"]
    // n:3 -> n:2에서 0 0 1 앞뒤로 모두 0,1을 끼워넣는다
    // [ "0" 0 "1" 0 "0" 1 "1"]

    public static int[] solution(int N) {
        StringBuilder sb = new StringBuilder();
        int idx;
        for (int n = 1; n <= N; n++) {
            idx = 0;
            if (n == 1) {
                sb.append(0);
                continue;
            }
            int originLength = sb.length();
            for (int cnt = 0; cnt < (originLength+1)/2; cnt++) {
                sb.insert(idx, 0);
                if (sb.length() > idx + 2) {
                    sb.insert(idx + 2, 1);
                    idx += 4;
                } else {
                    sb.append(1);
                    idx++;
                }
            }
        }
        char[] chs= sb.toString().toCharArray();
        int len = chs.length;
        int[] answer = new int[len];
        for(int i = 0; i < len; i++){
            answer[i] = Character.getNumericValue(chs[i]);
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(3)));
    }
}
