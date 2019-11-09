package test.라인;
public class Solution4 {

    private static int getDistance(int idx, int[]arr)
    {
        int leftDist;
        int rightDist;

        int i = idx;

        while( i >= 0 && arr[i] != 1){
            i--;
        }

        leftDist = idx - i;

        i = idx;

        while( i < arr.length && arr[i] != 1){
            i++;
        }
        rightDist = i - idx;

        return Math.min(leftDist, rightDist);
    }

    public static void main(String []args)
    {
        int a = 7;
        int [] arr = {1,0,1,0,0,0,1};

        int maxDistance = 0;

        for(int i = 0 ; i < arr.length;i++){

            if(arr[i] == 1)
                continue;

            maxDistance = Math.max(maxDistance, getDistance(i, arr));
        }
        System.out.println(maxDistance);
    }

}
