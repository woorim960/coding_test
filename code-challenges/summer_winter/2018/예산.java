import java.util.*;
// import java.io.*;

class Solution {
    public int solution(int[] d, int budget) {
        Arrays.sort(d);
        
        int cnt = 0;
        for (int m: d) {
            budget -= m;
            if (budget < 0) return cnt;
            cnt++;
        }
        return cnt;
    }
}
