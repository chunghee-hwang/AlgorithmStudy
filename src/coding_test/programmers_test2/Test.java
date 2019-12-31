package coding_test.programmers_test2;

import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Test {
    static class Document implements Comparable<Document>{
        int priority;
        int idx;

        public Document(int priorities, int idx) {
            this.priority = priorities;
            this.idx = idx;
        }

        @Override
        public int compareTo(Document o) {
            return o.priority - priority;
        }
    }
    public static int solution(int[] priorities, int location) {
        PriorityQueue<Document> priorityQueue = new PriorityQueue<>();
        Queue<Document> q = new LinkedList<>();
        for (int i = 0 ; i < priorities.length; i++) {
            Document doc= new Document(priorities[i],i);
            priorityQueue.add(doc);
            q.add(doc);
        };
        int order = 1;
        while(!q.isEmpty()){
            Document doc = q.remove();
            Document peek = null;
            if(!priorityQueue.isEmpty())
                peek = priorityQueue.peek();
            if(peek != null && peek.priority > doc.priority)
                q.add(doc);
            else if(doc.idx == location)
                break;
            else {
                priorityQueue.remove();
                order++;
            }
        }
        return order;
    }
    public static void main(String[] args)
    {
        int []pri = {1,1,9,1,1,1};
        System.out.println(solution(pri, 0));
    }
}
