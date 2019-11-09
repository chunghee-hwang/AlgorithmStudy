package test.라인;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;

public class Solution1 {

    private int getExecuteTime(Queue<Integer> queue) {
        int sum = 0;
        for (final int message : queue) {
            sum += message;
        }
        return sum;
    }

    private int getTotalExecuteTime(List<Queue<Integer>> queues){
        int maxTime = 0;
        int executeTime;
        for(final Queue<Integer> queue : queues){
            executeTime = getExecuteTime(queue);
            if(maxTime < executeTime){
                maxTime = executeTime;
            }
        }
        return maxTime;
    }

    public void solution() {
        //Scanner in = new Scanner(System.in);
        int a = 5;
        int b = 2;
        int[] c = {4, 3, 5, 2, 8};
        int queueExecuteTime;
        int idx;
        int minIdx;
        int minCnt;
        List<Queue<Integer>> queues = new ArrayList<>();
        for (int i = 0; i < b; i++) {
            queues.add(new LinkedBlockingQueue<>());
        }
        outerLoop:
        for (int i = 0; i < c.length; i++) {
            System.out.println(c[i]);
            for (Queue<Integer> q : queues) {
                if (q.isEmpty()) {
                    q.add(c[i]);
                    continue outerLoop;
                }
            }

            idx = 0;
            minIdx = idx;
            minCnt = getExecuteTime(queues.get(idx));
            for (Queue<Integer> q : queues) {
                if (minCnt > (queueExecuteTime = getExecuteTime(queues.get(idx)))) {
                    minCnt = queueExecuteTime;
                    minIdx = idx;
                }
                idx++;
            }
            queues.get(minIdx).add(c[i]);
        }

        System.out.println(getTotalExecuteTime(queues));
    }


    public static void main(String[] args) {
        new Solution1().solution();
    }

}
