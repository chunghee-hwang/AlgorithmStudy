class Solution {
    public String solution(String code) {
        int mode = 0;
        StringBuilder ret = new StringBuilder();
        char[] chs = code.toCharArray();
        for (int i = 0; i < code.length(); i++){
            char elem = chs[i];
            boolean isEven = i % 2 == 0;
            if (mode == 0) {
                if (elem != '1') {
                    if (isEven) {
                        ret.append(elem);
                    }
                } else {
                    mode = 1;
                }
            } else {
                if (elem != '1') {
                    if (!isEven) {
                        ret.append(elem);
                    } 
                } else {
                    mode = 0;
                }
            }
        }
        if (ret.length() == 0) {
            return "EMPTY";
        }
        return ret.toString();
    }
}