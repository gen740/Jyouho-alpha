#include <array>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

struct star {
    double m;
    double x, y, z;
    double px, py, pz;
    int flag;
};

void runge(star* st[3], double dt);
float fp();
float fx();


int main()
{
    // 変数の宣言
    double dt;
    // 変数の初期化
    dt = 0.0001;
}

void runge(star* st[3], double dt)
{
    double xa[3];
    double pa[3];
}
