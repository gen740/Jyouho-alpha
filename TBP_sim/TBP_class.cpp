#include "DataGen.hpp"
#include "TBP_class.hpp"

#include <array>
#include <cmath>
#include <cstdarg>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>

// todo function prototype

#define EXPORT_DATA_X(out_file)           \
    for (int j = 0; j < DIM; j++) {       \
        out_file << stars[i].x[j] << " "; \
    }

#define EXPORT_DATA_Y(out_file)           \
    for (int j = 0; j < DIM; j++) {       \
        out_file << stars[i].p[j] << " "; \
    }

// the global functions.
// the function of create random real
double Rand_0to1()
{
    static int counter = 0;
    static std::mt19937 engine(1);  // todo seed
    std::uniform_real_distribution<> dist(0.0, 1.0);
    return dist(engine);
}

// Construntors for star
// empty constructor for TBP class
star::star() {}

star::star(double input, ...)
{
    double n[DIM * 2];
    va_list args;
    va_start(args, input);
    for (int i = 0; i < DIM * 2; i++) {
        n[i] = va_arg(args, double);
    }
    m = input;
    for (int i = 0; i < DIM; i++) {
        x[i] = n[i];
        p[i] = n[DIM + i];
    }
}

star::star(bool rand_initialization)
{
    if (rand_initialization == true) {
        m = Rand_0to1() / 2.0 + 0.5;
        for (int i = 0; i < DIM; i++) {
            x[i] = Rand_0to1() - 0.5;
            p[i] = Rand_0to1() - 0.5;
        }
    }
}

// member function
void star::Show()
{
    std::cout << std::fixed;
    std::cout << std::setprecision(8)
              << "mass    : " << m << "\nposition: ";
    for (int i = 0; i < DIM; i++) {
        std::cout << x[i] << " ";
    }
    std::cout << "\nmomentum: ";
    for (int i = 0; i < DIM; i++) {
        std::cout << p[i] << " ";
    }
    std::cout << std::endl;
}

// constructor for TBP
TBP::TBP(star stars_input[])
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        stars[i] = stars_input[i];
        std::ofstream("../data/star" + std::to_string(i + 1) + ".csv");
    }
    file_open();
}

TBP::TBP(std::array<double, (NUMBER_OF_STAR * (1 + 2 * DIM))> data)
{
    int num = 1 + 2 * DIM;
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        stars[i].m = data[num * i + 0];  // todo modification
        for (int j = 0; j < DIM; j++) {
            stars[j].x[j] = data[num * i + j + 1];
        }
        for (int j = 0; j < DIM; j++) {
            stars[j].p[j] = data[num * i + j + 4];
        }
    }
}

// Other functions belong to TBP.
void TBP::file_open()
{
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        std::ofstream("../data/star" + std::to_string(i + 1) + ".csv");
        files[i].open("../data/star" + std::to_string(i + 1) + ".csv",
            std::ios::app);
    }
}

void TBP::file_close()
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
    static unsigned int counter = 0;
    file_open();
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        files[i] << std::fixed;
        files[i] << std::setprecision(8);
        EXPORT_DATA_X(files[i]);
        EXPORT_DATA_Y(files[i]);
        if (counter % 500 == 0) {
            files[i] << std::endl;
        } else {
            files[i] << "\n";
        }
    }
    counter++;
}

void TBP::Save_to_file(std::string to_file)
{
    static std::fstream output_file;
    if (to_file == "NULL") {
        Save();
    } else {
        output_file.open(to_file, std::ios::out | std::ios::in | std::ios::ate);
        for (int i = 0; i < NUMBER_OF_STAR; i++) {
            output_file << std::fixed;
            output_file << std::setprecision(8);
            for (int j = 0; j < DIM; j++) {
                output_file << stars[i].x[j] << " ";
            }
            for (int j = 0; j < DIM; j++) {
                output_file << stars[i].p[j] << " ";
            }
        }
        output_file.seekp(-1, std::ios::end);
        output_file << std::endl;
        output_file.close();
    }
}

void TBP::Save_to_file(std::fstream& to_file)
{
    static unsigned int counter = 0;
    for (int i = 0; i < NUMBER_OF_STAR; i++) {
        to_file << std::fixed;
        to_file << std::setprecision(8);
        for (int j = 0; j < DIM; j++) {
            to_file << stars[i].x[j] << " ";
        }
        for (int j = 0; j < DIM; j++) {
            to_file << stars[i].p[j] << " ";
        }
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
