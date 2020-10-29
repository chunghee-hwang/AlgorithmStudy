

import java.util.ArrayDeque;
//https://programmers.co.kr/learn/courses/30/lessons/43165
public class TargetNumber {
    private static class Data{
        int idx;
        int sign;
        int sum;
        private Data(int idx, int sign, int sum) {
            this.idx = idx;
            this.sign = sign;
            this.sum = sum;
        }
        static Data make(int i, int s, int s2){
            return new Data(i,s, s2);
        }
    }
    public int solution(int[] numbers, int target) {
        int cnt = 0;
        int n = numbers.length;
        ArrayDeque<Data> q = new ArrayDeque<>();
        q.add(Data.make(0,1, 0));
        q.add(Data.make(0,-1, 0));
        while(!q.isEmpty())
        {
            int size = q.size();
            for(int k=0; k <size; k++){
                Data data = q.remove();
                int idx = data.idx;
                int sum = data.sum;
                sum += (numbers[idx] * data.sign);
                if(idx == n-1){
                    if(sum == target) cnt++;
                }else{
                    q.add(Data.make(idx + 1, 1, sum));
                    q.add(Data.make(idx + 1, -1, sum));
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        System.out.println(new TargetNumber().solution(numbers, 3));
    }
}
