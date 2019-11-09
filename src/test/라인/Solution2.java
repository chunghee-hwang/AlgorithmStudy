package test.라인;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Solution2 {

    private static List<Integer> list = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> inputs = new ArrayList<>();
        int[] arr;
        while(sc.hasNext()){
            inputs.add(sc.nextInt());
        }
        arr = inputs.subList(0, inputs.size()-1).stream().mapToInt(i->i).toArray();
        permutation(arr, 0, arr.length, 3);
        System.out.println(list.get(inputs.get(inputs.size()-1)));
        sc.close();
    }

    static void permutation(int[] arr, int depth, int n, int r) {
        if(depth == r) {
            addPerm(arr);
            return;
        }

        for(int i=depth; i<n; i++) {
            swap(arr, depth, i);
            permutation(arr, depth + 1, n, r);
            swap(arr, depth, i);
        }
    }

    static void swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }

    static void addPerm(int[] arr) {
        StringBuilder str = new StringBuilder();
        for(int a : arr){
            str.append(a);
        }

        list.add(Integer.parseInt(str.toString()));
    }

}
