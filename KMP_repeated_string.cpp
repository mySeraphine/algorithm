//
// Created by Xiang_Duan on 2021/4/17.
//
#include <iostream>
#include <string>

class Solution {
public:
    bool repeatedSubstringPattern(std::string s) {
        if (s.length() == 1) {
            return false;
        } else if (s.length() == 2) {
            if (s[0] != s[1]) {
                return false;
            }
            return true;
        }
        int next[s.size()];
        get_next(next, s);
        int len = s.size();
        if (next[len - 1] != -1 && len % (len - (next[len - 1] + 1)) == 0)
            return true;
        return false;
    }

    void get_next(int *next, std::string &cp) {
        int j = -1;
        next[0] = -1;
        for (int i = 1; i < cp.length(); ++i) {
            while (j != -1 && cp[i] != cp[j + 1]) {
                j = next[j];
            }
            if (cp[i] == cp[j + 1]) {
                j++;
            }
            next[i] = j;
        }
    }
};

int main() {
    Solution s;
    std::cout << s.repeatedSubstringPattern("abab");

    return 0;
}
