package greedy;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

//https://programmers.co.kr/learn/courses/30/lessons/42883
public class MakeBigNumber {
    public static String solution(String number, int k) {
        int len = number.length();
        if (len == 1) return number;
        String[] strs = number.split("");
        Set<String> set =
                Stream.of(strs)
                        .sorted((o1, o2) -> Integer.parseInt(o2) - Integer.parseInt(o1))
                        .limit(k)
                        .collect(Collectors.toSet());
        System.out.println(set);

        for (int i = 0; i < strs.length && k > 0; i++) {
            if (!set.contains(strs[i])) {
                strs[i] = "";
                k--;
            }
        }
        return String.join("", strs);
    }

    public static void main(String[] args) {
        String answer = solution("4177252841", 4);
        System.out.println(answer);
    }
}
