package src.bfs_dfs;

import java.util.*;

//https://programmers.co.kr/learn/courses/30/lessons/43163

public class ChangeWords {
    private HashMap<String, Boolean> visit = new HashMap<>();

    List<String> getChangeable(String word, String[] words) {
        int wordLength = word.length();
        int wordsLength = words.length;
        BitSet bitSet = new BitSet();
        List<String> changeable = new LinkedList<>();
        char[] chs = word.toCharArray();
        String regex;
        for (int i = 0; i < wordLength; i++) {
            char[] a = chs.clone();
            a[i] = '.';
            regex = new String(a);
            for (int k = 0; k < wordsLength; k++) {
                if (bitSet.get(k)) continue;
                if (words[k].matches(regex) && !words[k].equals(word) && visit.get(words[k]) == null) {
                    changeable.add(words[k]);
                    bitSet.set(k);
                }
            }
        }
        return changeable;
    }

    public int solution(String begin, String target, String[] words) {
        Queue<String> q = new LinkedList<>();
        q.add(begin);
        visit.put(begin, true);
        int size;
        int cnt = 0;

        while (!q.isEmpty()) {
            size = q.size();
            for (int i = 0; i < size; i++) {
                List<String> changeable = getChangeable(q.remove(), words);
                cnt++;
                for (String s : changeable) {
                    if (visit.get(s) != null) continue;
                    if (s.equals(target)) {
                        return cnt;
                    }
                    visit.put(s, true);
                    q.add(s);
                }

            }
        }
        return 0;
    }

    public static void main(String[] args) {
        String begin = "hit";
        String target = "hhh";
        String[] words = "hhh, hht".split(", ");

        System.out.println(new ChangeWords().solution(begin, target, words));
    }
}
