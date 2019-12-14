package coding_test.네이버;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;

public class Solution3 {

    private class Document implements Comparable<Document>{
        int num;
        int requestTime;
        int page;

        public Document(int num, int requestTime, int page) {
            this.num = num;
            this.requestTime = requestTime;
            this.page = page;
        }

        @Override
        public String toString() {
            return "Document{" +
                    "num=" + num +
                    ", requestTime=" + requestTime +
                    ", page=" + page +
                    '}';
        }

        @Override
        public int compareTo(Document o) {
            if(this.page == o.page){
                return this.num - o.num;
            }
            return this.page - o.page;
        }
    }

    private Document getDocumentByRequestTime(int time, int[][]data){
        for(int[] request : data)
        {
            if(request[1] == time){
                return new Document(request[0], request[1], request[2]);
            }
        }
        return null;
    }

    public int[] solution(int[][] data)
    {
        Queue<Document> printQueue = new LinkedBlockingQueue<>();
        Queue<Document> waitQueue = new PriorityQueue<>();
        Queue<Document> completeQueue = new LinkedBlockingQueue<>();

        int time = 0;

        printQueue.add(new Document(data[0][0], data[0][1], data[0][2]));

        while(completeQueue.size() != data.length){

            Document waitDoc;

            Document peek;
            if(!printQueue.isEmpty() && (peek = printQueue.peek()).requestTime + peek.page<= time)
            {
                completeQueue.add(printQueue.remove());
            }

            waitDoc = getDocumentByRequestTime(time, data);

            if(printQueue.isEmpty() && !waitQueue.isEmpty()){
                printQueue.add(waitQueue.remove());
            }
            else
            {
                if(waitDoc!= null && waitDoc.num!= 1)
                    waitQueue.add(waitDoc);
            }

            time++;
        }

        return new ArrayList<>(completeQueue).stream().mapToInt(doc-> doc.num).toArray();

    }

    public static void main(String []args){
        int[][] data = {{1,0,5},{2,2,2},{3,3,1},{4,4,1},{5,10,2}};
        System.out.println(Arrays.toString(new Solution3().solution(data)));
    }
}
