package greedy;
//https://programmers.co.kr/learn/courses/30/lessons/42860

import java.util.Arrays;

public class JoyStick {
    private static boolean[] same;

    // dest와 src의 같은 알파벳 위치를 same 배열에 체크하는 함수
    private static int checkSameDigit(char[] src, char[] dest) {
        int len = src.length;
        int sameCnt = 0;
        same = new boolean[len];
        for (int i = 0; i < len; i++) {
            if (src[i] == dest[i]) {same[i] = true; sameCnt++;}
        }
        return sameCnt;
    }

    //위, 아래 키를 최소 횟수로 눌러 커서 위치의 알파벳을 변경하는 함수
    private static int rotateAlphabet(int cursor, char[] src, char[] dest) {
        char s = src[cursor];
        char d = dest[cursor];
        final char Z = 'Z';
        int diff1 = d - s; // A->Z 방향으로 이동할 때 커서 이동 횟수
        int diff2 = Z - d + 1; // Z->A 방향으로 이동할 때 커서 이동 횟수
        src[cursor] = d;
        same[cursor] = true;
        return Math.min(diff1, diff2);
    }

    //왼쪽, 오른쪽 키를 최소 횟수로 눌러 '알파벳이 같지 않은 위치'로 이동하는 함수
    private static int[] moveCursor(int cursor) {
        // {이전 커서와 이동한 커서와의 차이, 현재 커서 위치}
        int[] moveDiffAndDestCursor = new int[2];
        if (!same[cursor]) return moveDiffAndDestCursor;
        int len = same.length;
        int i,j;
        int diff1 = 0;
        int diff2 = 0;
        for(i = cursor; same[i]; i = (i+1)%len ){diff1++;} //오른쪽으로 이동할 시
        for(j =cursor; same[j]; j = (j-1<0)?len-1:j-1){diff2++;}//왼쪽으로 이동할 시

        //오른쪽으로 이동할 때가 더 효율적일 경우
        if(diff1 <= diff2){
            moveDiffAndDestCursor[0] = diff1;
            moveDiffAndDestCursor[1] = i;
        }
        //왼쪽으로 이동할 때가 더 효율적일 경우
        else{
            moveDiffAndDestCursor[0] = diff2;
            moveDiffAndDestCursor[1] = j;
        }
        return moveDiffAndDestCursor;
    }

    public static int solution(String name) {
        char[] dest = name.toCharArray();
        int len = dest.length;
        char[] src = new char[len];
        int cursor = 0;
        int cnt = 0;
        int digitChangeCompleteCnt; //알파벳 변경이 완료된 횟수
        int[] moveDiffAndDestCursor;
        Arrays.fill(src, 'A');
        digitChangeCompleteCnt = checkSameDigit(src, dest);

        //알파벳 변경횟수가 dest의 길이와 같아질때까지 반복
        while (len != digitChangeCompleteCnt) {
            // 1. 커서를 왼쪽 또는 오른쪽으로 알파벳이 같지 않은 위치로 이동
            moveDiffAndDestCursor = moveCursor(cursor);
            cnt+=moveDiffAndDestCursor[0];
            cursor = moveDiffAndDestCursor[1];
            cnt += rotateAlphabet(cursor, src, dest);

            // 2. 커서 위치에 있는 알파벳을 원하는 알파벳으로 변경
            digitChangeCompleteCnt++;
        }
        return cnt;
    }

    public static void main(String[] args) {
        System.out.println(solution("JEROEN"));
        System.out.println(solution("JAN"));
        System.out.println(solution("AZAAAZ"));
    }
}
