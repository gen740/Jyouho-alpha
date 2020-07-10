#include "TBP_class.hpp"
#include <array>
#include <cmath>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>

namespace fs = std::filesystem;

void star::Show()
{
    std::cout << std::fixed;
    std::cout << std::setprecision(8)
              << "mass    : " << m << std::endl
              << "position: "
              << x[0] << " "
              << x[1] << " "
              << x[2] << " \n"
              << "momentum: "
              << p[0] << " "
              << p[1] << " "
              << p[2] << " \n\n";
}

TBP::TBP(star stars_input[])
{
    fs::remove_all("data");
    fs::create_directory("data");
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        stars[i] = stars_input[i];
        std::ofstream("data/star" + std::to_string(i + 1) + ".csv");
        files[i].open("data/star" + std::to_string(i + 1) + ".csv",
            std::ios::out);
    }
}

TBP::~TBP()
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        files[i].close();
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
                    r_2 += std::pow(((stars[j].x[l]
                                         + K[i] * stars[j].kx[i][l])
                                        - (stars[k].x[l]
                                              + K[i] * stars[k].kx[i][l])),
                        2.0);
                }
                if (j != k) {
                    for (int l = 0; l < DIM; l++) {
                        // calculate runge
                        // forward kp
                        stars[j].kp[i + 1][l]
                            += -((G * stars[j].m * stars[k].m)
                                   * ((stars[j].x[l]
                                          + K[i] * stars[j].kx[i][l])
                                         - (stars[k].x[l]
                                               + K[i] * stars[k].kx[i][l]))
                                   / std::pow(r_2, 3 / 2))
                               * dt;
                        // forward kx
                        stars[j].kx[i + 1][l]
                            += ((stars[j].p[l] + K[i] * stars[j].kp[i + 1][l])
                                   / stars[j].m)
                               * dt;
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

void TBP::Save()
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        files[i] << std::fixed;
        files[i] << std::setprecision(8)
                 << stars[i].x[0] << " "
                 << stars[i].x[1] << " "
                 << stars[i].x[2] << " "
                 << stars[i].p[0] << " "
                 << stars[i].p[1] << " "
                 << stars[i].p[2] << std::endl;
    }
}

void TBP::Show()
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        std::cout << "Star number = " << i + 1 << std::endl;
        stars[i].Show();
    }
    std::cout << "---------------------------------------------------------"
              << "\n";
}
