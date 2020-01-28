package coding_test.쏘카;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;

public class Solution2 {

    public static String[] solution(String[][] friends, String user_id){
        HashMap<String, LinkedList<String>> map = new HashMap<>();
        HashSet<String> people = new HashSet<>();

        for(String[] friend : friends){
            String f0 = friend[0];
            String f1 = friend[1];
            people.add(f0);
            people.add(f1);
            LinkedList<String> get0 = map.get(f0);
            LinkedList<String> get1 = map.get(f1);
            if(get0 == null){
                get0 = new LinkedList<>();
               map.put(f0, get0);
            }
            if(get1 == null){
                get1 = new LinkedList<>();
                map.put(f1, get1);
            }
            get0.add(f1);
            get1.add(f0);
        }
        LinkedList<String> realFriends = map.get(user_id);
        LinkedList<String> recommended = new LinkedList<>();
        int cnt;
        int maxCnt = 0;
        for (String person : people) {
            if(person.equals(user_id)) continue;
            if(!realFriends.contains(person)){
                cnt = 0;
                LinkedList<String> otherFriends = map.get(person);
                for (String otherFriend : otherFriends) {
                    if(realFriends.contains(otherFriend)) cnt++;
                }
                if(maxCnt <= cnt){
                    if(maxCnt < cnt){
                        maxCnt = cnt;
                        recommended.clear();
                    }
                    recommended.add(person);
                }
            }
        }
        return recommended.toArray(new String[0]);
    }
    public static void main(String[] args) {
        String[][] friends  = {{"david", "frank"}, {"demi", "david"},{"frank", "james"},{"demi", "james"}, {"claire","frank"}};
        System.out.println(Arrays.toString(solution(friends, "david")));
    }
}
