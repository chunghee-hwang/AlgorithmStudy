package test.카카오인턴;

import java.util.Arrays;
import java.util.HashMap;

//결과 :정확성 100% 효율성 0%
public class Solution4 {
    static HashMap<Long, Boolean> rooms = new HashMap<>();
    static long getEmptyRoom(long want){
        while(rooms.get(++want)!=null);
        return want;
    }

    public static long[] solution(long k, long[] room_number) {

        long want;
        for(int i = 0; i <room_number.length; i++){
            want = room_number[i];
            if((rooms.get(want)) != null) {
                want = getEmptyRoom(want);
            }
            rooms.put(want, true);
            room_number[i] = want;
        }
        return room_number;
    }
    public static void main(String[] args) {
        int k = 10;
        long []room_number = {1,3,4,1,3,1};

        System.out.println(Arrays.toString(solution(k, room_number)));
    }
}
