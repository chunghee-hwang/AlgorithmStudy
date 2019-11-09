package test.부스트캠프;
// 프로그래밍1

// 문제 설명
// 문제)

// 자연수가 들어있는 배열 arr가 매개변수로 주어집니다. 배열 arr안의 숫자들 중에서 앞에 있는 숫자들부터 뒤에 중복되어 나타나는 숫자들 중복 횟수를 계산해서 배열로 반환하도록 solution 함수를 완성해주세요. 만약 중복되는 숫자가 없다면 배열에 -1을 채워서 반환하세요.

// 입출력 예 #1
// arr = [1, 2, 3, 3, 3, 4, 4]에서 3은 3번, 4는 2번씩 나타나므로 [3, 2]를 반환합니다.

// 입출력 예 #2
// arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]이면 2가 3회, 4가 2회, 5가 3회 나타나므로 [3, 2, 3]를 반환합니다.

// 입출력 예 #3
// [3, 5, 7, 9, 1]에서 중복해서 나타나는 숫자는 없으므로 [-1]을 반환합니다.

// 제한사항
// 배열 arr의 길이는 1 이상 100 이하의 자연수입니다.
// 배열 arr의 원소는 1 이상 100 이하의 자연수입니다.

import java.util.HashMap;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.ArrayList;
class Test {
    public int[] solution(int[] param) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int p : param)
        {
            Integer cnt = map.get(p);
            if(cnt == null)
            {
                map.put(p, 1);
            }
            else
            {
                cnt = cnt.intValue() + 1;
                map.put(p, cnt);
            }
        }
        SortedSet<Integer> keys = new TreeSet<Integer>(map.keySet());
        // System.out.println(map);
        ArrayList<Integer> list = new ArrayList<Integer>(map.values());
        ArrayList<Integer> anslist = new ArrayList<Integer>();
        // System.out.println(list);

        for(Integer l : list)
        {
            if(l.intValue() > 1)
                anslist.add(l);
        }
        // System.out.println(list);

        if(anslist.isEmpty())
            anslist.add(-1);
         // System.out.println(anslist);

        return anslist.stream().mapToInt(i->i).toArray();
    }
}

