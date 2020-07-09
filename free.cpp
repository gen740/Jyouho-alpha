#include <iostream>

constexpr int r = 4;


int main()
{
    int a[4] = {4, 5, 2, 3};

    teat(a);
    for (int i = 0; i < r; i++) {
        std::cout << a[i];
    }

    int x = 0;
    return 0;
}
