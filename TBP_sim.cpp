#include <array>
#include <cmath>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <string>

constexpr int NUMBER_OF_STAR = 3;
constexpr int DIM = 3;
constexpr double G = 1;
constexpr std::array<double, 4> K = {1, 1 / 2, 1 / 2, 1};

// Class Difinitions
class star
{
public:
    double m;
    std::array<double, DIM> x;
    std::array<double, DIM> p;
    std::array<std::array<double, DIM>, 5> kx;
    std::array<std::array<double, DIM>, 5> kp;
    int flag = 0;
};

class TBP
{
public:  // members
    star stars[NUMBER_OF_STAR];
    float dt = 0.0001;

public:  // constructor
    TBP(star stars[]);

public:  // class functions
    void runge();
    void Save();
};


// Other Functions
void Show_data(star stars[]);


int main()
{
    star stars[NUMBER_OF_STAR] = {
        {1, 0.5, 0.4, 0.6, 0.0, 0.0, 0.0},
        {1, 0.4, 0.6, 0.1, 0.0, 0.0, 0.0},
        {1, 0.7, 0.1, 0.5, 0.0, 0.0, 0.0},
    };

    Show_data(stars);
    TBP test(stars);
    for (int i = 0; i < 10000000; i++) {
        test.runge();
        if (i % 100000 == 0) {
            std::cout << i << std::endl;
        }
    }
    Show_data(test.stars);
    return 0;
}

TBP::TBP(star stars_input[])
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        stars[i] = stars_input[i];
    }
}

void TBP::runge()
{
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < NUMBER_OF_STAR; j++) {
            for (int k = 0; k < DIM; k++) {
                // initialize
                stars[j].kp[i + 1][k] *= 0;
                stars[j].kx[i + 1][k] *= 0;
            }
            for (int k = 0; k < NUMBER_OF_STAR; k++) {
                // calculate r^2
                double r_2 = 0;
                for (int l = 0; l < DIM; l++) {
                    r_2 += std::pow(((stars[j].x[l] + K[i] * stars[j].kx[i][l])
                                        - (stars[k].x[l] + K[i] * stars[k].kx[i][l])),
                        2.0);
                }
                if (j != k) {
                    for (int l = 0; l < DIM; l++) {
                        // calculate runge
                        // forward kp
                        stars[j].kp[i + 1][l]
                            += -((G * stars[j].m * stars[k].m)
                                   * ((stars[j].x[l] + K[i] * stars[j].kx[i][l])
                                         - (stars[k].x[l] + K[i] * stars[k].kx[i][l]))
                                   / std::pow(r_2, 3 / 2))
                               * dt;
                        // forward kx
                        stars[j].kx[i + 1][l]
                            += ((stars[j].p[l] + K[i] * stars[j].kp[i + 1][l])
                                   / stars[j].m)
                               * dt;
                        //
                        //
                    }
                }
            }
        }
    }
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        for (int l = 0; l < DIM; l++) {
            stars[i].p[l] += (stars[i].kp[1][l]
                                 + 2 * stars[i].kp[2][l]
                                 + 2 * stars[i].kp[3][l]
                                 + stars[i].kp[4][l])
                             / 6;

            stars[i].x[l] += (stars[i].kx[1][l]
                                 + 2 * stars[i].kx[2][l]
                                 + 2 * stars[i].kx[3][l]
                                 + stars[i].kx[4][l])
                             / 6;
        }
    }
}

void Show_data(star stars[])
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        std::cout << std::fixed;
        std::cout << std::setprecision(10)
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
