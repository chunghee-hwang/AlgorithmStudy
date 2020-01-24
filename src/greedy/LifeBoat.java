package greedy;

import java.util.Arrays;

//https://programmers.co.kr/learn/courses/30/lessons/42885?language=java
public class LifeBoat {
    public static int solution(int[] people, int limit) {
        int len = people.length;
        int boatCnt = 0;
        Arrays.sort(people);
        int s = 0;
        int e = len-1;

        while(s+1 <= e){
            if(people[s]+people[e] <= limit){
                len-=2;
                s++;
                boatCnt++;
            }
            e--;
        }
        boatCnt+=len;
        return boatCnt;
    }
    public static void main(String[] args) {
        int []people = {10, 50, 50, 60, 70, 70, 80};
        // 50 50 70 80
        // 10 50 50 60 70 70 80
        System.out.println(solution(people, 100));
    }
}
