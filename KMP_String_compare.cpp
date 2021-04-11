#include <string>
#include <iostream>

void get_next(std::string &s, int *next) {
    int j = -1;
    next[0] = -1;
    for (int i = 1; i < s.length(); ++i) {
        while (j != -1 && s[i] != s[j + 1])
            j = next[j];

        if (s[i] == s[j + 1])
            j++;

        next[i] = j;
    }
}

int kmp(std::string &s, std::string &cp) {
    
    int m = s.length(), n = cp.length();
    if (n==0)
        return -1;
    
    int next[cp.length()];
    get_next(cp, next);

    int j = -1;
    for (int i = 0; i < m; ++i) {
        while (j != -1 && s[i] != cp[j + 1])
            j = next[j];            //如果匹配失败，在模式串中回退到next[j]位置，重新开始匹配，直至j=-1

        if (s[i] == cp[j + 1])
            j++;                    //如果匹配成功,j就向后移一位
        if (j == n - 1)
            return i - n + 1;       //返回模式串在主串中开头的索引

    }
    return -1;
}


int main() {
    std::string s = "ababaa";
    std::string cp="a";

    std::cout<<kmp(s,cp);
}
