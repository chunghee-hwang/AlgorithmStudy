package test.라인;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution6 {

    private static final String sharp = "#";
    private static final String dot = ".";

    private static List<String> makeNumber(int width, int number)
    {
        int height = 2 * width -1;
        String str = "";
        switch(number)
        {

            case 0:
                String head = sharp.repeat(width);
                String middle = sharp + dot.repeat(width-2);
                str += head + "\n";
                for(int i = 0 ; i < height; i++){
                    str += middle + "#\n";
                }
                str += head + "\n";
                System.out.println(str);

                break;
        }

        return Arrays.stream(str.split("\n")).collect(Collectors.toList());
    }

    public static void main(String []args)
    {
        int length = 4;
        String sort = "TOP";
        int width = 5;
        int number = 123;
        System.out.println(makeNumber(width, 0));
    }

}
