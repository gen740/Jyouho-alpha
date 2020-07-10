#include "TBP_class.hpp"
#include <array>
#include <filesystem>
#include <iostream>
#include <string>

// Other Functions
void Show_data(star stars[]);
namespace fs = std::filesystem;

int main()
{
    std::fstream file;
    star stars[NUMBER_OF_STAR] = {
        {1, 0.5, 0.4, 0.0, 0.0, 0.0, 0.0},
        {1, 0.4, 0.6, 0.0, 0.0, 0.0, 0.0},
        {1, 0.7, 0.1, 0.0, 0.0, 0.0, 0.0},
    };

    Show_data(stars);
    TBP test(stars);
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


void Show_data(star stars[])
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        std::cout << std::fixed;
        std::cout << std::setprecision(8)
                  << "Star number = " << i + 1 << std::endl
                  << "mass    : " << stars[i].m << std::endl
                  << "position: "
                  << stars[i].x[0] << " "
                  << stars[i].x[1] << " "
                  << stars[i].x[2] << " \n"
                  << "momentum: "
                  << stars[i].p[0] << " "
                  << stars[i].p[1] << " "
                  << stars[i].p[2] << " \n\n";
    }
    std::cout << "---------------------------------------------------------"
              << "\n";
}
