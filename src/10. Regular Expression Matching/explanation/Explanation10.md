# Approach Overview:

**Python Logic Explanation**

Create a 2D DP array dp of size (len(text)+1) x (len(pattern)+1) initialized to False.

Base case:
dp[-1][-1] = True → empty string matches empty pattern.

Traverse i backward from len(text) to 0, and j backward from len(pattern)-1 to 0.

For each pair (i, j):

first_match checks if the current characters match or if pattern has a dot ..

If the next pattern character (pattern[j+1]) is *, there are two options:

Skip * and its preceding char → dp[i][j+2]

Use * if first_match → first_match and dp[i+1][j]

Else, if no *, just move both pointers one step → first_match and dp[i+1][j+1].

The result is dp[0][0] → does full string match full pattern?

Key Points:

Handles * as "zero or more" of the previous char.

Works in reverse for easier dependency management.

Time Complexity: O(m × n)
Space Complexity: O(m × n)


**C++ Logic Explanation**

Define a 2D boolean array dp[text.length()+1][pattern.length()+1].

Base case:
dp[text.length()][pattern.length()] = true.

Iterate i backward over text, j backward over pattern.

For each (i, j):

Compute first_match → text[i] == pattern[j] or pattern[j] == '.'.

If next pattern char is *:

Either ignore the * and its previous char → dp[i][j+2].

Or if current char matches → first_match && dp[i+1][j].

Otherwise, move both pointers → first_match && dp[i+1][j+1].

Return dp[0][0].

Key Points:

The bottom-up DP eliminates recursion and stack overflow risks.

Java’s character indexing (charAt) matches Python’s string indexing logic.

Time Complexity: O(m × n)
Space Complexity: O(m × n)

**Java Logic Explanation**


Use a 2D boolean array dp[n+1][m+1] (where n = text length, m = pattern length).

Base case:
dp[0][0] = true → empty text matches empty pattern.

Fill dp table:

For each i from 0 → n, and j from 1 → m:

If pattern char p[j-1] == '*', then:

Either skip * (dp[i][j-2])

Or match one occurrence if previous character matches →
(i>0 && (s[i-1]==p[j-2] || p[j-2]=='.') && dp[i-1][j])

Else:

Match current char → (i>0 && dp[i-1][j-1] && (s[i-1]==p[j-1] || p[j-1]=='.'))

Return dp[n][m] → final match result.

Key Points:

Uses static 2D array for performance.

Carefully handles 1-based DP indexing to match 0-based string indexing.

Uses memset to initialize DP array to false.

Time Complexity: O(m × n)
Space Complexity: O(m × n)