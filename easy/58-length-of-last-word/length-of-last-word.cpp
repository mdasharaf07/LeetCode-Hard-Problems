class Solution {
public:
    int lengthOfLastWord(string s) {
        int count=0;
        int s1=s.size();
        int i=s1-1;
        while(i>=0 && s[i] == ' ') i--;
        while(i>=0 && s[i] != ' '){
            count++;
            i--;
        } 
        return count;
    }
};