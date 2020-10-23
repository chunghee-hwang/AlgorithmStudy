package src.greedy;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Queue;
//https://programmers.co.kr/learn/courses/30/lessons/42884
public class TrafficCamera {
    private int[][] routes;
    private boolean isIntersect(int idx1, int idx2) {
        int[] first = routes[idx1];
        int[] second = routes[idx2];
        int f0 = first[0];
        int f1 = first[1];
        int s0 = second[0];
        int s1 = second[1];

        return (f0 <= s0 && s0 <= f1 && f1<=s1) || (s0 <= f0 && f0 <= s1 && s1<=f1) || (f0 < s0 && s1 < f1) || (s0 < f0 && f1 < s1);
    }

    public int solution(int[][] routes) {
        Arrays.sort(routes, Comparator.comparingInt(o -> o[0]));
        this.routes = routes;
        int n = routes.length;
        int cnt = 0;
        Queue<Integer> q = new ArrayDeque<>();
        for (int route = 0; route < n; route++) {
            int[] r = routes[route];
            if(r[0] <= r[1]) q.add(route);
        }
        Queue<Integer> group = new ArrayDeque<>();
        boolean []visit = new boolean[n];
        while (!q.isEmpty()) {
            Integer route = q.remove();
            if(visit[route]) {
                group.clear();
                visit = new boolean[n];
                cnt++;
            }

            boolean sameGroup = true;
            for (Integer r : group) {
                if (!isIntersect(r, route)) {
                    sameGroup = false;
                    break;
                }
            }
            if(sameGroup)
                group.add(route);
            else{
                q.add(route);
            }
            visit[route] = true;
        }
        return ++cnt;
    }
    public static void main(String[] args) {
        int[][] routes = {{-20,15},{-14,-5},{-18,-13},{-5,-3}};
        System.out.println(new TrafficCamera().solution(routes));
    }
}
