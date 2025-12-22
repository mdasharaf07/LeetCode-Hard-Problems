class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length();
        int n = t.length();

        vector<vector<unsigned long long>> dp(
            m + 1, vector<unsigned long long>(n + 1, 0));

        for (int i = 0; i <= m; i++) {
            dp[i][n] = 1;
        }

        for (int sIndex = m - 1; sIndex >= 0; sIndex--) {
            for (int tIndex = n - 1; tIndex >= 0; tIndex--) {
                dp[sIndex][tIndex] = dp[sIndex + 1][tIndex];

                if (s[sIndex] == t[tIndex]) {
                    dp[sIndex][tIndex] += dp[sIndex + 1][tIndex + 1];
                }
            }
        }

        return dp[0][0];
    }
};