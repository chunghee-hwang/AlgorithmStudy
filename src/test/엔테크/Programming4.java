package test.엔테크;

public class Programming4 {

    private static final long divider = 10007;

    public static int dp(long n, int k){
        if(n == 1 || k == 0) return 1;
        if(n*n == k) return 0;
        if(k == 1) return (int)((n*n) % divider);
        return 0;
    }

    public static int solution(int n, int k) {
        int answer = 2;
        return answer;
    }

    public static void main(String[] args) {

    }
}
