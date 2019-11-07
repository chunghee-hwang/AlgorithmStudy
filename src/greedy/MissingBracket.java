package greedy;

import java.util.Scanner;
import java.util.StringTokenizer;
// https://www.acmicpc.net/problem/1541

//세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

//그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

//괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
public class MissingBracket {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        StringTokenizer tokenizer = new StringTokenizer(input, "-+", true);
        int sum = 0;
        int partSum = 0;
        boolean isMinus = false;
        while (tokenizer.hasMoreTokens()) {
            String token = tokenizer.nextToken();
            if(token.equals("-")){
                if (!isMinus)
                    isMinus = true;
                else{
                    sum += partSum;
                    partSum = 0;
                }
            }
            else if (!token.equals("+")) {
                if (isMinus) {
                    partSum -= Integer.parseInt(token);
                } else {
                    partSum += Integer.parseInt(token);
                }
            }
        }
        sum += partSum;
        System.out.println(sum);
    }
}
