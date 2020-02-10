package simulation;

import java.util.*;

//https://programmers.co.kr/learn/courses/30/lessons/60060
public class SearchingLyrics {
    private int[] result;
    private String[] words;
    private Query[] queryList;
    private static class Query {
        String value;
        int idx;
        int len;
        boolean isBack;

        Query(String value, int idx, int len, boolean isBack) {
            this.value = value;
            this.idx = idx;
            this.len = len;
            this.isBack = isBack;
        }

        boolean isChild(Query query){
            if(len != query.len || isBack != query.isBack) return false;
            if(isBack) return query.value.endsWith(value);
            else return query.value.startsWith(value);
        }


        boolean isMatch(String word){
            if(len != word.length()) return false;
            if(isBack) return word.endsWith(value);
            else return word.startsWith(value);
        }

        @Override
        public String toString() {
            return "Query{" +
                    "value='" + value + '\'' +
                    ", idx=" + idx +
                    ", len=" + len +
                    ", isBack=" + isBack +
                    '}';
        }
    }

    private void sortQueries() {
        Arrays.sort(queryList, (o1, o2) -> {
            String v1 = o1.value;
            String v2 = o2.value;
            int len1 = o1.len;
            int len2 = o2.len;
            boolean b1 = o1.isBack;
            boolean b2 = o2.isBack;
            int k1 = 0, k2 = 0;
            if(b1) k1 = 1;
            if(b2) k2 = 1;
            if(b1 != b2) return k1-k2;
            if(len1 != len2) return len1-len2;
            return v1.compareTo(v2);
        });
        System.out.println(Arrays.toString(queryList));
    }

    private void saveQueries(String[] queries, int n) {
        for (int i = 0; i < n; i++) {
            String value = queries[i];
            boolean isBack = value.charAt(0) == '?';
            int len = value.length();
            if (isBack) {
                value = value.substring(value.lastIndexOf('?') + 1, len);
            } else {
                value = value.substring(0, value.indexOf('?'));
            }
            Query query = new Query(value, i, len, isBack);
            queryList[i] = query;
        }
    }
    private boolean []visit;
    private void search(int parent, int cur, int n, ArrayDeque<String> matchedWords){
        if(cur == n || visit[cur]) return;
        visit[cur] = true;
        Query query = queryList[cur];
        if(parent == -1){
            matchedWords = new ArrayDeque<>();
            for (String word : words) {
                if(query.isMatch(word))
                    matchedWords.add(word);
            }
        }
        else{
            int size = matchedWords.size();
            for(int k =0; k < size; k++){
                String matchedWord = matchedWords.remove();
                if(query.isMatch(matchedWord))
                    matchedWords.add(matchedWord);
            }
        }
        result[query.idx] = matchedWords.size();
        for(int i = cur+1; i < n; i++){
            if(query.isChild(queryList[i])){
                search(cur,i,n,new ArrayDeque<>(matchedWords));
            }else break;
        }
    }
    public int[] solution(String[] words, String[] queries) {
        int n = queries.length;
        this.words = words;
        queryList = new Query[n];
        saveQueries(queries, n);
        sortQueries();
        visit = new boolean[n];
        result= new int[n];
        for(int i =0; i < n; i++) search(-1, i, n, null);
        return result;
    }

    public static void main(String[] args) {
        String[] words = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
        String[] queries = {"fro??", "????o", "fr???", "fro???", "pro?"};
        System.out.println(Arrays.toString(new SearchingLyrics().solution(words, queries)));
    }
}
