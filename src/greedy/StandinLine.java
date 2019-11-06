package greedy;

import java.util.Scanner;
//https://www.acmicpc.net/problem/1138
public class StandinLine {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 사람 수 (키는 1~n)
        int []d = new int[11];
        for(int i = 1; i <= n; i++){ //i : 줄세울 사람의 키
            int x =  sc.nextInt(); //x: 자신보다 키가 더 큰 사람들의 수
            int count = 0;

            for(int j = 1; j <= n; j++){ //j: 줄세울 사람의 위치
                if(count == x && d[j] == 0)
                {
                    d[j] = i;
                    break;
                }
                if(d[j] == 0)
                    count++;
            }
        }
        for(int i = 1; i <=n ; i++){
            System.out.print(d[i]+" ");
        }
    }
}
