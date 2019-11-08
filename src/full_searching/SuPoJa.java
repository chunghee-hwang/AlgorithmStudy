package full_searching;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.IntStream;

// https://programmers.co.kr/learn/courses/30/lessons/42840
public class SuPoJa {
    public int[] solution(int[] answers) {
        int []patt1 = {1,2,3,4,5};
        int []patt2 = {2,1,2,3,2,4,2,5};
        int []patt3 = {3,3,1,1,2,2,4,4,5,5};
        int []counts = {0,0,0};
        int idx1, idx2, idx3;
        for(int i = 0; i < answers.length; i++)
        {
            idx1 = (i%patt1.length);
            idx2 = (i%patt2.length);
            idx3 = (i%patt3.length);
            if(answers[i] == patt1[idx1]) counts[0]++;
            if(answers[i] == patt2[idx2]) counts[1]++;
            if(answers[i] == patt3[idx3]) counts[2]++;
        }
        int max = IntStream.of(counts).max().getAsInt();
        List<Integer> list = new LinkedList<>();
        for(idx1 = 0; idx1 < counts.length; idx1++)
            if(counts[idx1] == max) list.add(idx1+1);
        return list.stream().mapToInt(i->i).toArray();
    }

    public static void main(String[] args) {
        int []answers = {1,3,2,4,2};
        System.out.println(Arrays.toString(new SuPoJa().solution(answers)));
    }
}
