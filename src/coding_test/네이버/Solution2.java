
package coding_test.네이버;
public class Solution2 {

    private char[][] firstDimensionToSecondDimension(final int N, final String[] array){
        char[][] d = new char[N][N];
        char[] row;
        for(int i = 0; i < N; i++){
            row = array[i].toCharArray();
            System.arraycopy(row, 0, d[i], 0, N);
        }
        return d;
    }

    private boolean dropTheBall(final int N, char[][]d, int startPos){
        int i = 0;
        int j = startPos;
        int starCnt = 0;
        while(i < N && starCnt < 2){
            switch (d[i][j]){
                case '#':
                    i++;
                    break;
                case '>':
                    j++;
                    break;
                case '<':
                    j--;
                    break;
                case '*':
                    i++;
                    starCnt++;
                    break;
            }
        }
        if(i >= N){
            return true;
        }
        return false;
    }

    public int solution(String[] drum)
    {
        int answer = 0;
        final int N = drum.length;
        char[][]d = firstDimensionToSecondDimension(N, drum);
        for(int i = 0 ; i < N; i++) {
            if(dropTheBall(N, d, i))
            {
                answer++;
            }
        }
        return answer;
    }
    public static void main(String []args)
    {
        String[] drum =
                {"######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"};
        System.out.println(new Solution2().solution(drum));
    }
}
