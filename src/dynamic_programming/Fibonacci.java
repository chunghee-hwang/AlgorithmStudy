package dynamic_programming;

public class Fibonacci {
    private static long []d = new long[100];

    static long fibonacci(int x){
        if(x == 1) return 1;
        if(x == 2) return 1;
        if(d[x] != 0) return d[x]; //이미 구한 값은 가져온다. 이 한 줄 안넣으면 시간복잡도는 O(2^n). 넣으면 O(n)
        return d[x] = fibonacci(x-1) + fibonacci(x-2);
    }

    public static void main(String[] args) {
        System.out.println(fibonacci(50));
    }
}
