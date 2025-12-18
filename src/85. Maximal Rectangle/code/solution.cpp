class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int rows = matrix.size(), cols = matrix[0].size();

        // given a row X cols binary matrix of "char", i wasted my 1hour due to
        // neglecting that its a matrix of char.
        // have to find the max area rectangle which consist of only 1s.
        // thought of a O(n^4) sol that is like for each 1 we found we would be
        // traversing
        // downwards while keeping in check of the right neighbors and updating
        // maxArea till we found a zero or reach the downward end. and the right
        // neighbor check would come in use when we would shift towards right.
        // because we would know which is the max downward index or u can say
        // the length of our increased breadth rect. but that won't be much of a
        // optimization cuz we would now need info on the curr lengths cells
        // neighbor.

        // return bruteForce(matrix);

        // this sloppy approach of mine could be used if applied with DP due to
        // overcounting of
        //   subrectangles (small rect present inside our maxArea rect or any
        //   bigger rect)
        //  but thinkin of stack solution like applying histograms by increasing
        //  the x-axis. lets assume last row's border be x-axis and all above
        //  columns cells be histogram bars/bins then would apply that max
        //  rectangle in histo approach by stack. and would increase the x-axis
        //  like now x-axis is at second last row's border.

        vector<int> height(cols, 0);
        int maxArea = 0;

        for (int i = 0; i < rows; i++) {
            // build histogram for this row
            for (int j = 0; j < cols; j++) {
                height[j] = (matrix[i][j] == '1') ? height[j] + 1 : 0;
            }

            // apply largest rectangle in histogram algorithm
            stack<int> st;
            for (int j = 0; j <= cols; j++) {
                int h = (j == cols ? 0 : height[j]);
                while (!st.empty() && h < height[st.top()]) {
                    int top = st.top();
                    st.pop();
                    int width = st.empty() ? j : j - st.top() - 1;
                    maxArea = max(maxArea, height[top] * width);
                }
                st.push(j);
            }
        }
        return maxArea;
    }

private:
    int bruteForce(vector<vector<char>>& matrix) {
        int rows = matrix.size(), cols = matrix[0].size();

        // auto check = [&](int a, int b)->bool{
        //     return min(a,b)>=0 && a<rows && b<cols;
        // };

        int maxArea = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == '1') {
                    int max_len_index = rows - 1;
                    for (int y = j; y < cols; y++) {
                        if (matrix[i][y] == '0')
                            break;
                        for (int x = i; x <= max_len_index; x++) {
                            if (matrix[x][y] == '0') {
                                max_len_index = x - 1;
                                break;
                            }
                        }
                        maxArea =
                            max(maxArea, (max_len_index - i + 1) * (y - j + 1));
                    }
                }
            }
        }
        return maxArea;
    }
};