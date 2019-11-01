package dynamic_programming;
import static java.lang.Math.max;
// https://programmers.co.kr/learn/courses/30/lessons/43105
public class IntegerTriangle {

    public int solution(int [][]triangle){
        int answer = 0;
        int [][]ans = new int[triangle.length][triangle.length];

        ans[0][0] = triangle[0][0]; //7

        for(int i = 1; i < triangle.length; i++){
            for(int j = 0; j <= i; j++){
                if(j == 0){ //왼쪽 테두리 요소
                    // (바로 오른쪽위에까지의 누적합+ 자기자신) 저장
                    ans[i][j] = ans[i-1][j] + triangle[i][j];
                }
                else if( i == j){ //오른쪽 테두리 요소
                    //  (바로 왼쪽위에까지위 누적합 + 자기자신) 저장
                    ans[i][j] = ans[i-1][j-1] + triangle[i][j];
                }
                else { // 그 외의 요소
                    //(바로 왼쪽위에까지의 누적합+자기자신)와 (바로 오른쪽위에까지의 누적합+자기자신)중 큰 값 저장
                    ans[i][j] = max(ans[i-1][j-1] + triangle[i][j], ans[i-1][j] + triangle[i][j]);
                }
                if(i == triangle.length -1){//answer배열의 마지막 행의 값들 중 가장 큰값을 구함
                    answer = max(answer, ans[i][j]);
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[][] triangle = {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
        System.out.println(new IntegerTriangle().solution(triangle));
    }
}
