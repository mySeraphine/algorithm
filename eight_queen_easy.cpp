//
// Created by Xiang_Duan on 2021/3/22.
//
#include <cmath>
#include <iostream>

using namespace std;

const int MAX = 8;


bool check(int k, int y[]) {
    for (int i = 1; i < k; i++) {
        if ((abs(k - i) == abs(y[k] - y[i])) || (y[i] == y[k])) {
            return false;
        }
    }
    return true;
}

int main() {
    int y[MAX+1] = {0};

    int cnt = 0;
    int row = 1;
    while (row > 0) {
        y[row]++;
        while ((y[row] <= MAX) && (!check(row, y))) {
            y[row] += 1;
        }
        if (y[row] <= MAX) {
            if (row == MAX) {
                cnt++;
            } else {
                row++;
            }
        } else {
            y[row] = 0;
            row--;
        }
    }
    cout << cnt;
    return 0;
}
