class Solution {
    public String solution(String[] str_list, String ex) {
        String test = "abcd";
        StringBuilder sb = new StringBuilder();
        for (String str : str_list) {
            if (!str.contains(ex)) {
                sb.append(str);
            }
        }
        return sb.toString();
    }
}