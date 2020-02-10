package heap;

import java.util.*;
//https://programmers.co.kr/learn/courses/30/lessons/42628
public class BinaryHeap {
    private static class BinaryComparator implements Comparator<Integer>{
        private int direction = 1;
        private Queue<Integer> parentQueue;
        private void changeToASC(){
            if(this.direction == 1) return;
            direction=1;
            refreshParentQueue();
        }
        private void changeToDESC(){
            if(this.direction == -1) return;
            direction = -1;
            refreshParentQueue();
        }
        private void refreshParentQueue(){
            int size = parentQueue.size();
            for(int i = 0; i < size; i++) parentQueue.add(parentQueue.poll());
        }

        void setParentQueue(Queue<Integer> parentQueue) {
            this.parentQueue = parentQueue;
        }

        @Override
        public int compare(Integer o1, Integer o2) {
            return direction*(o1-o2);
        }
    }

    private static class BinaryPriorityQueue extends PriorityQueue<Integer> {
        BinaryPriorityQueue(BinaryComparator comparator) {
            super(comparator);
        }

        private void pollMax(){
            ((BinaryComparator)comparator()).changeToDESC();
            poll();
        }
        private void pollMin(){
            ((BinaryComparator)comparator()).changeToASC();
            poll();
        }
    }

    public int[] solution(String[] operations) {
        int[] answer = {0,0};
        BinaryComparator comparator = new BinaryComparator();
        BinaryPriorityQueue q = new BinaryPriorityQueue(comparator);
        comparator.setParentQueue(q);
        for (String operation : operations) {
            String []cmd = operation.split(" ");
            String cmd1 = cmd[0];
            int cmd2 = Integer.parseInt(cmd[1]);
            switch (cmd1){
                case "D":
                    if(q.isEmpty()) continue;
                    switch (cmd2){
                        case 1:
                            q.pollMax();
                            break;
                        case -1:
                            q.pollMin();
                            break;
                    }
                    break;
                case "I":
                    q.add(cmd2);
                    break;
            }
        }
        if(q.isEmpty()) return answer;
        answer[0] = Collections.max(q);
        answer[1] = Collections.min(q);
        return answer;
    }
    public static void main(String[] args) {
       String[] operations = {"I 19", "I 18", "I 17","I 5","I 5","D 1","D -1"};
        System.out.println(Arrays.toString(new BinaryHeap().solution(operations)));

    }
}
