package coding_test.쏘카;

public class Solution3
{
    private int[] nums;
    private boolean[] visit;
    private final int BIG_NUMBER = 100001;
    private int toNext(int idx, int cnt, int n){
        if(idx<0 || idx>=n) return BIG_NUMBER;
        if(visit[idx]) return BIG_NUMBER;
        visit[idx] = true;
        cnt++;
        if(idx == n-1) return cnt;
        return Math.min(toNext(idx-nums[idx], cnt, n), toNext(idx+nums[idx], cnt, n));
    }
    public int solution(int[] nums){
        this.nums = nums;
        int n = nums.length;
        visit = new boolean[n];
        int cnt = toNext(0,-1,nums.length);
        return cnt != BIG_NUMBER? cnt:-1;
    }
    public static void main(String[] args) {
        int []nums = {4,1,2,3,1,0,5};
        System.out.println(new Solution3().solution(nums));
    }
}
