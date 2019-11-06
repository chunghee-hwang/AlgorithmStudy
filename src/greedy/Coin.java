package greedy;

import java.util.Scanner;

// https://www.acmicpc.net/problem/11047
//준규가 가지고 있는 동전은 총 N종류이고,
// 각각의 동전을 매우 많이 가지고 있다.
//동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
// 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
public class Coin {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;
        int []kinds = new int[n];
        int i;
        for(i = 0 ; i < n; i++){
            kinds[i] = sc.nextInt();
        }
        for(i = n-1; i >=0 && k != 0; i--){
            result += k / kinds[i];
            k %= kinds[i];
        }

        System.out.println(result);
    }

}
