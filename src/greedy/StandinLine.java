package greedy;

import java.util.Scanner;

public class StandinLine {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int []d = new int[11];
        for(int i = 1; i <= n; i++){
            int x =  sc.nextInt();
            int count = 0;

            for(int j = 1; j <= n; j++){
                if(count == x && d[j] == 0){
                    d[j] = i;
                    break;
                }
                if(d[j] == 0)
                    count++;
            }
        }
        for(int i = 1; i <=n ; i++){
            System.out.print(d[i]+" ");
        }
    }
}
