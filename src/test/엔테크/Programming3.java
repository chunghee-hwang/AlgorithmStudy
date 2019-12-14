package test.엔테크;

import java.util.Stack;

public class Programming3 {

    private boolean checkIsValid(String[] inputs){
        final String bigOpen = "[";
        final String bigClose = "]";
        final String middleOpen = "{";
        final String middleClose = "}";
        final String smallOpen = "(";
        final String smallClose = ")";

        Stack<String> stack = new Stack<>();


        for (String s : inputs) {
            if(!s.equals(bigOpen) && !s.equals(bigClose) && !s.equals(middleOpen) && !s.equals(middleClose) && !s.equals(smallOpen) && !s.equals(smallClose))
                continue;
            if(stack.isEmpty()) {stack.push(s); continue;};
            String peek = stack.peek();
            boolean cond1 = peek.equals(bigOpen) && (s.equals(middleClose) || s.equals(smallClose));
            boolean cond2 = peek.equals(middleOpen) && (s.equals(smallClose));
            boolean cond3 = peek.equals(smallOpen) && (s.equals(middleOpen) || s.equals(bigOpen));
            boolean cond4= peek.equals(middleOpen) && (s.equals(bigOpen));
            boolean cond7 = (peek.equals(bigOpen) && s.equals(bigOpen)) || (peek.equals(middleOpen) && s.equals(middleOpen)) || (peek.equals(smallOpen) && s.equals(smallOpen));
            if(peek.equals(bigOpen) && s.equals(bigClose))
                stack.pop();
            else if(peek.equals(middleOpen) && s.equals(middleClose))
                stack.pop();
            else if(peek.equals(smallOpen) && s.equals(smallClose))
                stack.pop();
            else if(cond1 | cond2 | cond3 | cond4 | cond7) return false;
            else stack.push(s);
        }
        return stack.isEmpty();
    }
    public boolean solution(String input) {
        input = input.replaceAll("\\d|-|\\+|\\*|/","");
        String []inputs = input.split("");
        return checkIsValid(inputs);
    }
    public static void main(String[] args) {
        System.out.println(new Programming3().solution("[{( )}]"));
    }
}
