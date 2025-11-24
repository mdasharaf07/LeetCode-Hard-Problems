class Solution {
    public boolean solve(int index1, int index2, String text, String pattern) {
        if (index1 < 0 && index2 < 0) return true;
        if (index2 < 0 && index1 >= 0) return false;
        if (index1 < 0 && index2 >= 0) {
            for (int i = 0; i <= index2; i++) {
                if (pattern.charAt(i) != '*') return false;
            }
            return true;
        }

        if (text.charAt(index1) == pattern.charAt(index2) || pattern.charAt(index2) == '?') {
            return solve(index1 - 1, index2 - 1, text, pattern);
        }

        if (pattern.charAt(index2) == '*') {
            return solve(index1 - 1, index2, text, pattern) || solve(index1, index2 - 1, text, pattern);
        }

        return false;
    }

    public boolean isMatch(String s, String p) {
        int n1 = s.length();
        int n2 = p.length();
        return solve(n1 - 1, n2 - 1, s, p);
    }
}