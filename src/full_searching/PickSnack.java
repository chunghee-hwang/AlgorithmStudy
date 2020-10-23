package src.full_searching;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW8Wj7cqbY0DFAXN&categoryId=AW8Wj7cqbY0DFAXN&categoryType=CODE

public class PickSnack {
    private static void pickSnack(int t, int[]snacks, int n, int limit){
        List<Integer> snackBack = new LinkedList<>();
        for(int i= 0 ; i < n; i++){
            for(int k = i+1; k < n; k++){
                int sum = snacks[i] + snacks[k];
                if(sum <= limit) snackBack.add(sum);
            }
        }
        if(snackBack.size() != 0) System.out.println("#"+t+" "+Collections.max(snackBack));
        else System.out.println(-1);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
        int n, limit;
        int []snacks = new int[1000];
        for (int t = 1; t <= testcase; t++) {
            n = sc.nextInt();
            limit = sc.nextInt();
            for (int k = 0; k < n; k++) snacks[k] = sc.nextInt();
            pickSnack(t, snacks, n, limit);
        }
    }
}
