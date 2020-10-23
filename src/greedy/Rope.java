package src.greedy;

import java.util.Comparator;
import java.util.Scanner;
import java.util.stream.IntStream;

// https://www.acmicpc.net/problem/2217
/*
N(1≤N≤100,000)개의 로프가 있다.
이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다.
각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

각 로프들에 대한 정보가 주어졌을 때,
이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.
모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
단, 각각의 로프는 한 개씩만 존재한다.
* */
public class Rope {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int n = sc.nextInt();
        int i;
        int []ropes = new int[n];
        for(i = 0; i < n; i++){
            ropes[i] = sc.nextInt();
        }

        ropes = IntStream.of(ropes).boxed().sorted(Comparator.reverseOrder()).mapToInt(v->v).toArray();
        int maxWeight = 0;
        int weight;

        for(i = 0; i < n; i++){
            weight = ropes[i] * (i+1);
            if(maxWeight < weight) maxWeight = weight;
        }
        System.out.println(maxWeight);
    }
}
