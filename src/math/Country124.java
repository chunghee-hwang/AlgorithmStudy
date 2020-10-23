package src.math;

public class Country124 {
    //https://programmers.co.kr/learn/courses/30/lessons/12899
    public static String solution(int n) {
        StringBuilder sb = new StringBuilder();
        int[] map = {4,1,2};
        int share = n; // 몫
        int rest;
        while(share != 0){
            rest = share%3;
            share/=3;
            if(rest == 0) share-=1;
            sb.insert(0, map[rest]);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(solution(13));
    }
}
