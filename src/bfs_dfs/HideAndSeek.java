

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// https://www.acmicpc.net/problem/1697
public class HideAndSeek {
    static int bfs(int n, int m){
        final int MAX_VALUE = 100001;
        boolean []visit = new boolean[MAX_VALUE];

        int time = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(n);

        while(true){
            int size = q.size();

            for(int i=0; i<size; i++) {
                n = q.peek();
                q.remove();
                if(n == m)
                    return time;
                if(n > 0 && !visit[n-1]) {
                    q.add(n-1);
                    visit[n-1] = true;
                }
                if(n < 100000 && !visit[n+1]) {
                    q.add(n+1);
                    visit[n+1] = true;
                }
                if(n*2 <= 100000 && !visit[n*2]) {
                    q.add(n*2);
                    visit[n*2] = true;
                }
            }
            time++;
        }
    }

    public static void main(String[] args) {
        System.out.println("수빈위치와 동생위치를 입력:");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        System.out.println(bfs(n, m));
    }

}
