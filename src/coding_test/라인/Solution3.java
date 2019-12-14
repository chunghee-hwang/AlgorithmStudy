package coding_test.라인;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;

public class Solution3 {

    static class Participate{
        int inTime;
        int outTime;
        Participate(int inTime, int outTime) {
            this.inTime = inTime;
            this.outTime = outTime;
        }
    }

    public static void main(String []args)
    {
        int N = 2;

        ArrayList<Participate> partis = new ArrayList<>();
        partis.add(new Participate(5,15));
        partis.add(new Participate(0,10));

        partis.sort((o1, o2) -> {
            if (o1.inTime == o2.inTime) {
                return o1.outTime - o2.outTime;
            }
            return o1.inTime - o2.inTime;
        });

        List<Queue<Participate>> queues = new ArrayList<>();
        Iterator<Participate> iter = partis.iterator();
        Iterator<Queue<Participate>> iter2;
        Participate parti;
        while(iter.hasNext()){
            parti = iter.next();
            if(queues.isEmpty()){
                Queue<Participate> queue = new LinkedBlockingQueue<>();
                queues.add(queue);
            }
            iter2 = queues.iterator();
            while(iter2.hasNext()){
                Queue<Participate> queue = iter2.next();
                Participate in = queue.peek();
                if(in == null){
                    queue.add(parti);
                    break;
                }
                if(in.outTime <= parti.inTime){
                    queue.remove();
                    queue.add(parti);
                    break;
                }
                Queue<Participate> newQueue = new LinkedBlockingQueue<>();
                queues.add(newQueue);
                newQueue.add(parti);
                break;
            }

        }

        System.out.println(queues.size());

    }

}
