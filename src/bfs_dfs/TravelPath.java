package bfs_dfs;

import java.util.*;

//https://programmers.co.kr/learn/courses/30/lessons/43164
public class TravelPath {
    private List<String> paths = new LinkedList<>();

    private List<Integer> getAvailable(boolean[] visit, String departure, String[][] tickets) {
        List<Integer> available = new LinkedList<>();
        for (int i = 0; i < tickets.length; i++) {
            if (departure.equals(tickets[i][0]) && !visit[i])
                available.add(i);
        }
        return available;
    }

    private boolean isAllVisited(boolean[] visit) {
        for (boolean b : visit) {
            if (!b) return false;
        }
        return true;
    }

    private void dfs(boolean[] visit, List<String> path, String[][] tickets, String departure) {
        List<Integer> available = getAvailable(visit, departure, tickets);
        path.add(departure + " ");
        for (Integer a : available) {
            boolean[] v = visit.clone();
            List<String> p = new LinkedList<>(path);
            if (isAllVisited(v))
                return;
            v[a] = true;
            dfs(v, p, tickets, tickets[a][1]);
        }

        if (path.size() == tickets.length + 1)
            paths.add(String.join("", path));
    }

    public String[] solution(String[][] tickets) {
        boolean[] visit = new boolean[tickets.length];
        List<String> path = new LinkedList<>();
        dfs(visit, path, tickets, "ICN");
        paths.sort(String::compareTo);
        System.out.println(paths);
        return paths.get(0).split(" ");
    }

    public static void main(String[] args) {
        String[][] tickets =
                {{"ICN", "SFO"},
                        {"ICN", "ATL"},
                        {"SFO", "ATL"},
                        {"ATL", "ICN"},
                        {"ATL", "SFO"}};
        System.out.println(Arrays.toString(new TravelPath().solution(tickets)));
    }
}