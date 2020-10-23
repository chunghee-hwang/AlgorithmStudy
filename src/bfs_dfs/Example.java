package src.bfs_dfs;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

//https://programmers.co.kr/learn/courses/30/lessons/43162
public class Example {
    private boolean[] flags;
    private LinkedList<Integer>[] links;

    private int getUnvisited(){
        for(int i = 0 ; i < flags.length; i++){
            if(!flags[i]) return i;
        }
        return -1;
    }

    private void bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        flags[start] = true;
        while(!q.isEmpty()){
            int x = q.remove();
            for(int i = 0; i < links[x].size(); i++){
                int y = links[x].get(i);
                if(!flags[y])
                {
                    q.add(y);
                    flags[y] = true;
                }
            }
        }
    }

    private void dfs(int x){
        if(flags[x]) return;
        flags[x] = true;
        for(int i = 0; i < links[x].size(); i++){
            int y = links[x].get(i);
            dfs(y);
        }
    }

    public int solution(int n, int[][] computers) {
        links = new LinkedList[n];
        flags = new boolean[n];
        for(int i = 0; i < n; i++)
            links[i] = new LinkedList<>();

        for(int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++)
                if (y != x && computers[y][x] == 1) {
                    links[y].add(x);
                }
        }
        System.out.println(Arrays.toString(links));
        int unvisited;
        int cnt = 0;
        while((unvisited = getUnvisited()) != -1){
            //dfs(unvisited);
            bfs(unvisited);
            cnt++;
        }


        return cnt;
    }

    public static void main(String []args)
    {
        int n = 3;
        int [][]computers = {
                {1,1,0},
                {1,1,0},
                {0,0,1}};
        System.out.println(new Example().solution(n, computers));
    }
}
