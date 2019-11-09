package test.카카오인턴;

//결과 :정확성 100% 효율성 0%
public class Solution5 {

    public static int solution(int[] stones, int k) {
        int answer = 0;
        int i = 0;
        int n = stones.length;

        while (true) {
            int cnt = 0;
            while (stones[i] == 0) {
                cnt++;
                i++;
                if (i == n) {
                    i = n - 1;
                    break;
                }
            }
            if (cnt >= k)
                break;
            if (stones[i] != 0)
                stones[i]--;
            if (i == n - 1)
                answer++;
            i = (i + 1) % n;

        }


        return answer;
    }

    public static void main(String[] args) {
        int[] stones = {2, 4, 5, 3, 2, 1, 4, 2, 5, 1};
        int k = 3;
        System.out.println(solution(stones, k));
    }
}
