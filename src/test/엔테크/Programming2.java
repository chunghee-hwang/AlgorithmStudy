package test.엔테크;

import java.util.HashSet;
import java.util.Set;

public class Programming2 {
    public static int solution(long n) {
        String[] strs = (n + "").split("");
        Set<Integer> set = new HashSet<>();
        for (String ch : strs) {
            set.add(Integer.valueOf(ch));
        }
        int cnt = 0;
        for (Integer i : set) {
            if(i == 0) continue;
            if(n%i == 0) cnt++;
        }

        return cnt;
    }

    public static void main(String[] args) {
        System.out.println(solution(1230));
    }
}
