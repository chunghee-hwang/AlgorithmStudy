package test.엔테크;

public class Programming1 {
    public static int solution(int a, int b, int budget) {

        int maxAMulti = budget / a;
        int cnt = 0;
        for(int multiA = 0; multiA <= maxAMulti; multiA++){
            if((budget - a*multiA)%b == 0) cnt++;
        }
        System.out.println(cnt);
        return cnt;
    }
    public static void main(String[] args) {
        solution(3000, 5000, 23000);
    }
}
