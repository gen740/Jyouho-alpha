#include "TBP_class.hpp"
#include <array>
#include <filesystem>
#include <iostream>
#include <string>

// Other Functions
namespace fs = std::filesystem;

int main()
{
    std::fstream file;
    star stars[NUMBER_OF_STAR] = {
        {1, 0.5, 0.4, 0.0, 0.0, 0.0, 0.0},
        {1, 0.4, 0.6, 0.0, 0.0, 0.0, 0.0},
        {1, 0.7, 0.1, 0.0, 0.0, 0.0, 0.0},
    };

    TBP test(stars);
    test.Show();
    std::ofstream("data/options.txt");
    file.open("data/options.txt");
    file << "{ 'NUMBER_OF_STAR': " << NUMBER_OF_STAR << std::endl
         << ",'DIM': " << DIM << std::endl
         << ",'test':535,}" << std::endl;
    file.close();
    for (int i = 0; i < 100000; i++) {
        test.runge();
        if (i % 10 == 0) {
            std::cout << i << std::endl;
            test.Save();
        }
    }
    test.Show();
    return 0;
}
