package src.full_searching;

public class Palindrome {
    private static int palind(char[] chs, int left, int right, int n)
    {
        if(left <0 || left >= n || right <0 || right>=n)
            return 1;

        if(chs[left] == chs[right]){
            return Math.max(right-left+1, palind(chs, left-1, right+1,n));
        }
        return 1;
    }
    public static int solution(String s)
    {
        char[] chs = s.toCharArray();
        int n = s.length();
        int maxLength = 0;
        for(double pivot = 0.5; pivot <n; pivot+=0.5d){
            int newPalindLength;
            double diff;
            if(Math.floor(pivot)!=pivot){
                diff = 0.5d;
            }
            else{
                diff = 1d;
            }
            newPalindLength = palind(chs, (int)(pivot-diff), (int)(pivot+diff), n);
            if(maxLength < newPalindLength){
                maxLength = newPalindLength;
            }
        }
        return maxLength;
    }
    public static void main(String[] args) {
        System.out.println(solution("aaaa"));
        System.out.println(solution("aabaa"));
    }
}
