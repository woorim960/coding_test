// 1 solutionx
class Solution {
    boolean solution(String s) {
        s = s.toUpperCase();

        return s.chars().filter( e -> 'P'== e).count() == s.chars().filter( e -> 'Y'== e).count();
    }
}

// 2 solution
class Solution {
    boolean solution(String s) {
        int cntP = 0;
        int cntY = 0;
        
        s = s.toUpperCase();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'P') {
                cntP++;
            } else if (s.charAt(i) == 'Y') {
                cntY++;
            }
        }

        return cntP == cntY;
    }
}
