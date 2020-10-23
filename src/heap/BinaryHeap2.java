package src.heap;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class BinaryHeap2 {
    private final int modeMax = 1;
    private final int modeMin = -1;
    private int heapMode = modeMin;
    private Comparator<int[]> comparator = Comparator.comparingInt(o -> o[0]);
    private PriorityQueue<int[]> switchHeapToMinOrMax(PriorityQueue<int[]> heap, int heapMode)
    {
        if(this.heapMode == heapMode) return heap;
        for (int[] elem : heap) elem[0]*=-1;
        PriorityQueue<int[]> switchedHeap = new PriorityQueue<>(comparator);
        switchedHeap.addAll(heap);
        this.heapMode = heapMode;
        return switchedHeap;
    }

    public int[] solution(String[] operations) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(comparator);
        for (String operation : operations) {
            String []cmd = operation.split(" ");
            String op = cmd[0];
            int operand = Integer.parseInt(cmd[1]);
            switch (op){
                case "I":
                    if(heapMode == modeMin)
                        heap.add(new int[]{operand, operand});
                    else if(heapMode == modeMax)
                        heap.add(new int[]{-operand, operand});
                    break;
                case "D":
                    heap = switchHeapToMinOrMax(heap, operand);
                    heap.poll();
                    break;
            }

        }

        if(heap.isEmpty())
            return new int[]{0,0};
        else{
            heap = switchHeapToMinOrMax(heap, modeMax);
            int maxValue = heap.peek()[1];
            heap = switchHeapToMinOrMax(heap, modeMin);
            int minValue = heap.peek()[1];
            return new int[]{maxValue, minValue};
        }
    }

    public static void main(String[] args) {
        int[] answer = new BinaryHeap2().solution(new String[]{"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"});
        System.out.println(Arrays.toString(answer));
    }
}
