package src.hash;

import java.util.BitSet;
import java.util.Scanner;

public class WriteAndErase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BitSet bs = new BitSet();
        int n = sc.nextInt();
        for (int t = 0; t < n; t++) {
            int cnt = 0;
            char[] chs = sc.next().toCharArray();
            for (char ch : chs) {
                if (bs.get(ch)) {
                    bs.clear(ch);
                    cnt--;
                } else {
                    bs.set(ch);
                    cnt++;
                }
            }
            System.out.println(bs);
            System.out.println(cnt);
            bs.clear();
        }
    }
}
