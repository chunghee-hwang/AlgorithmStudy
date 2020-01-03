package dynamic_programming;

import java.util.Scanner;

//https://www.acmicpc.net/problem/1149
public class RGBStreet {
    private static int[][] houses;
    private static int minCostSum = Integer.MAX_VALUE;
    public static void solution(int k, int N, int [] selectedCost, int [] selectedColor)
    {
        if(k > N) {
            int costSum  = 0;
            for (int cost : selectedCost) costSum += cost;
            if(minCostSum > costSum) minCostSum = costSum;
            return;
        }
        int prevSelectedColor = selectedColor[k-1];
        for(int i = 1; i <= 3;i++) {
            if(prevSelectedColor == i)
                continue;
            selectedCost[k] = houses[k][i];
            selectedColor[k] = i;
            System.out.println(selectedCost[k]);
            solution(k+1, N, selectedCost, selectedColor);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        houses = new int[N + 1][4];
        int i;
        for (i = 1; i <= N; i++) {
            int[] colors = {0, sc.nextInt(), sc.nextInt(), sc.nextInt()};
            houses[i] = colors;
        }
        int[] selectedCost = new int[N+1];
        int[] selectedColor = new int[N + 1];
        selectedColor[0] = 0;
        selectedCost[0] = 0;
        solution(1, N, selectedCost, selectedColor);
        System.out.println(minCostSum);
    }
}
