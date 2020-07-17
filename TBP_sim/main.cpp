#include "DataGen.hpp"
#include "TBP_class.hpp"

#include <array>
#include <iostream>
#include <string>

// Other Functions

int main()
{
    star stars[3];
    for (int i = 0; i < 3; i++) {
        star tempstar(true);
        stars[i] = tempstar;
    }
    TBP test(stars);
    test.Show();
    test.Save_to_file();

    // Random_Generate(20000);
    // Calcdata_for_learning(10);
}
