//a easy solution of postfix_expression translation
#include <iostream>
#include <string>
#include <stack>

int level(char op) {
    if (op == '+' || op == '-') {
        return 1;
    } else if (op == '*' || op == '/') {
        return 2;
    }
    return 0;
}

int main() {
    std::stack<char> ops;
    std::string str;
    std::cin >> str;
    for (char e:str) {
        if (e >= '0' && e <= '9') {
            std::cout << e;
        } else if (e == '(')
            ops.push(e);
        else if (e == ')') {

            while (ops.top() != '(') {
                std::cout << ops.top();
                ops.pop();
            }
            if (ops.top()=='('){
                ops.pop();
            }
        } else {
            if (ops.empty() || ops.top() == '(') {
                ops.push(e);
            } else {
                while (level(ops.top()) > level(e)){
                    std::cout<<ops.top();
                    ops.pop();
                }
                if (level(ops.top())<=level(e)){
                    ops.push(e);
                }
            }
        }
    }
    while (!ops.empty()){

        std::cout<<ops.top();
        ops.pop();
    }
}
