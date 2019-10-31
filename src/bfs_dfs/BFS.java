package bfs_dfs;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
//너비 우선 탐색
public class BFS {

    private static void bfs(int start, LinkedList<Integer>[] a){
        boolean []c = new boolean[8];
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        c[start] = true;

        while(!q.isEmpty()){
            int x = q.remove();
            System.out.print(x+" ");
            for(int i = 0; i < a[x].size(); i++){
                int y = a[x].get(i);
                if(!c[y]){
                    q.add(y);
                    c[y] = true;
                }
            }
        }
    }




    public static void main(String []args){
        LinkedList<Integer>[] a = new LinkedList[8];
        for(int i = 0 ; i < 8; i++){
            a[i] = new LinkedList<>();
        }
        a[1].add(2);
        a[2].add(1);

        a[1].add(3);
        a[3].add(1);

        a[2].add(3);
        a[3].add(2);

        a[2].add(4);
        a[4].add(2);

        a[2].add(5);
        a[5].add(2);

        a[3].add(6);
        a[6].add(3);

        a[3].add(7);
        a[7].add(3);

        a[4].add(5);
        a[5].add(4);

        a[6].add(7);
        a[7].add(6);

        System.out.println(Arrays.toString(a));
        bfs(1, a);
    }
}
