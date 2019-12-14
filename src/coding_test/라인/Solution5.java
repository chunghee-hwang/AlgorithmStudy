package coding_test.라인;
public class Solution5 {
    private static int[][] initArray(int n, int m){

        int[][] arr = new int[n][m];


        for(int i = 0 ; i < n; i++){
            arr[i][0] = 1;
        }
        for(int j = 0 ; j < m; j++){
            arr[0][j] = 1;
        }

        return arr;
    }

    public static void main(String []args)
    {
        int n = 9;
        int m = 9;
        int x = 3;
        int y = 3;

        if(x <0 || x > n || y <0 || y > m){
            System.out.println("fail");
        }

        int [][]arr = initArray(n,m);
        int i = 1, j;
        while(i <=y){
            j = 1;
            while(j <=x)
            {
                arr[i][j] = arr[i-1][j] + arr[i][j-1];
                j++;
            }
            i++;
        }

        System.out.println(x+y);
        System.out.println(arr[y][x]);

    }

}
