class Solution {
    public String solution(int n) {
        String result = "";
        for (int i = 1; i <= n; i++) {
            result += i % 2 == 1 ? "수" : "박";
        }
        return result;
    }
}
