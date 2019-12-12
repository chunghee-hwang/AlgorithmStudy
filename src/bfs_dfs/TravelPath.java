package bfs_dfs;

import java.util.LinkedList;
import java.util.List;

//https://programmers.co.kr/learn/courses/30/lessons/43164
public class TravelPath {

    private List<Integer> getAvailable(boolean[] visit, String departure, String[][] tickets){
        List<Integer> available = new LinkedList<>();
        for(int i = 0; i < tickets.length; i++){
            if(departure.equals(tickets[i][0]) && !visit[i])
                available.add(i);
        }
        return available;
    }

    boolean isAllVisited(boolean[] visit){
        for (boolean b : visit) {
            if(!b) return false;
        }
        return true;
    }

    private void dfs(boolean[] visit, String[][] tickets, String departure){
        List<Integer> available = getAvailable(visit, departure, tickets);
        System.out.println(departure);
        for (Integer a : available) {

            boolean[] v = visit.clone();
            if(isAllVisited(v))
                return;
            v[a] = true;
            dfs(v, tickets, tickets[a][1]);
        }
    }

    public String[] solution(String[][] tickets) {
        String[] answer = {};
        boolean []visit = new boolean[tickets.length];
        dfs(visit, tickets, "ICN");
        return answer;
    }

    public static void main(String[] args) {
        String[][] tickets =
                {{"ICN", "SFO"},
                        {"ICN", "ATL"},
                        {"SFO", "ATL"},
                        {"ATL", "ICN"},
                        {"ATL","SFO"}};
        new TravelPath().solution(tickets);
    }
}
