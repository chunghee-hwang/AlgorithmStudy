package bfs_dfs;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// https://www.acmicpc.net/problem/1697
public class HideAndSeek2 {

    static boolean[] visit = new boolean[100001];
    static Queue<Integer> q = new LinkedList<>();

    public static void main(String[] args) {
        System.out.println("수빈위치와 동생위치를 입력:");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); //5
        int m = sc.nextInt(); //17
        q.add(n);
        int time = 0;
        outer : while (true) {
            int qSize = q.size();
            for(int i = 0; i < qSize; i++){
                int x = q.remove();
                if(x == m) break outer;
                int x2 = x-1;
                if(x2 >= 0 && !visit[x2]) {
                    q.add(x2);
                    visit[x2] = true;
                }
                x2 = x+1;
                if(x2 <= 100000 && !visit[x2]) {
                    q.add(x2);
                    visit[x2] = true;
                }
                x2 = x*2;
                if(x2 <= 100000 && !visit[x2]){
                    q.add(x2);
                    visit[x2] = true;
                }
            }
            time++;
        }
        System.out.println("time: " + time);
    }

}
