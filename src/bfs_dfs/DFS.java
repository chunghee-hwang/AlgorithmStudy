package bfs_dfs;

import java.util.Arrays;
import java.util.LinkedList;

//깊이 우선 탐색
public class DFS {
    private static void dfs(int x, boolean[] c, LinkedList<Integer>[] a){
        if(c[x])
            return;
        c[x] = true;
        System.out.print(x+" ");
        for(int i = 0 ; i < a[x].size(); i++){
            int y = a[x].get(i);
            dfs(y, c, a);
        }
    }

    public static void main(String []args){

        boolean []c = new boolean[8];
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
        dfs(1, c, a);
    }

}
