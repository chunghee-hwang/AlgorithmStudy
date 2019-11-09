package test.카카오인턴;

import java.util.*;
//결과 :정확성 100% 효율성 검사 없음
public class Solution2 {
    public static int[] solution(String s) {
        Set <Integer>set = new LinkedHashSet<>();
        int i;
        String[] k = s.split("},");
        List<int[]> elems = new LinkedList<>();
        for(i = 0 ; i < k.length; i++){
            k[i] = String.join(" ", k[i].split(","));
            k[i] = k[i].replaceAll("\\D+", " ");
            String []split = k[i].split(" ");
            int[] elem = new int[split.length-1];
            for(int j = 1; j < split.length; j++){
                elem[j-1] = Integer.parseInt(split[j]);
            }
            elems.add(elem);
        }

        elems.sort(Comparator.comparingInt(o -> o.length));

        for(int[]e : elems){
            for(i = 0 ; i <e.length; i++) set.add(e[i]);
        }

        int[] answer = new int[set.size()];
        i = 0;
        for(Integer v : set){
            answer[i++] = v;
        }
        return answer;
    }
    public static void main(String[] args) {
        String s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";
        System.out.println(Arrays.toString(solution(s)));
    }
}
