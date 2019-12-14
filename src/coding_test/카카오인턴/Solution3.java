package coding_test.카카오인턴;

import java.util.*;

//결과 :정확성 20% 효율성 검사 없음
public class Solution3 {

    private static boolean isMatch(String id, String banned_id){
        char[] chs = id.toCharArray();
        char[] chs2 = banned_id.toCharArray();
        int n = chs.length;
        if(n != chs2.length) return false;
        for(int i = 0; i < n; i++){
            if(chs2[i] == '*') continue;
            if(chs[i] != chs2[i]) return false;
        }
        return true;
    }

    public static int solution(String[] user_id, String[] banned_id) {
        Set<Set<String>> set = new HashSet<>();
        //List<List<String>> set = new LinkedList<>();
        for(int i = 0; i < banned_id.length; i++){
            Set<String> banSet = new HashSet<>();
            for(int j = 0; j < user_id.length; j++){
                if(isMatch(user_id[j], banned_id[i])){
                    banSet.add(user_id[j]);
                }
            }
            set.add(banSet);
        }
        return set.size();
    }
    public static void main(String[] args)
    {
        String[] user_id = {"abc123","frodo",  "crodo",  "frodoc", "fradi"};
        String[] banned_id = {"fr*d*", "******","*rodo", "******"};
        solution(user_id, banned_id);
    }
}
