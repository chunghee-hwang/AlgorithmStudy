package src.dynamic_programming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
//https://codeup.kr/problem.php?id=3007
public class MemoryTest {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] sums = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        int i;
        int num;
        for (i = 1; i < n + 1; i++) {
            num = Integer.parseInt(st.nextToken());
            if (i > 1) sums[i] = sums[i - 1] + num;
            else sums[i] = num;
        }
        System.out.println(Arrays.toString(sums));
        for (i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(sums[e]- sums[s-1]);
        }
    }
}
