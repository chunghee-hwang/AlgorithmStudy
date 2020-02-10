package graph;

import java.util.ArrayDeque;
import java.util.LinkedList;
//https://programmers.co.kr/learn/courses/30/lessons/49189
public class FarthestNode {
    private LinkedList<Integer>[] edges;
    private boolean[] isVisit;
    private void makeGraph(int n, int[][]edge){
        edges = new LinkedList[n+1];
        isVisit = new boolean[n+1];
        for (int[] e : edge) {
            int v1 = e[0];
            int v2 = e[1];
            LinkedList<Integer> edge1 = edges[v1];
            LinkedList<Integer> edge2 = edges[v2];
            if(edge1 == null) {
                edge1 = new LinkedList<>();
                edges[v1] = edge1;
            }
            if(edge2 == null) {
                edge2 = new LinkedList<>();
                edges[v2] = edge2;
            }
            edge1.add(v2);
            edge2.add(v1);
        }
    }

    private int visit(){
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(1);
        isVisit[1] = true;
        int depth = -1;
        int maxDepth = 0;
        int maxDepthNodeCnt = 0;
        while(!q.isEmpty()){
            int size = q.size();
            depth++;
            if(maxDepth < depth){
                maxDepth = depth;
                maxDepthNodeCnt = size;
            }
            for(int i = 0 ; i < size; i++){
                int vertex = q.remove();
                for (Integer nextVertex : edges[vertex]) {
                    if(!isVisit[nextVertex]) {
                        q.add(nextVertex);
                        isVisit[nextVertex] = true;
                    }
                }
            }
        }
        return maxDepthNodeCnt;
    }

    public int solution(int n, int[][] edge) {
        makeGraph(n,edge);
        return visit();
    }
    public static void main(String[] args) {
        int n = 6;
        int [][]vertex = {{3,6},{4,3},{3,2},{1,3},{1,2},{2,4},{5,2}};
        System.out.println(new FarthestNode().solution(n,vertex));
    }
}
