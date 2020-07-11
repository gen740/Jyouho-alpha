#pragma once
#include <array>
#include <fstream>

constexpr int NUMBER_OF_STAR = 3;
constexpr int DIM = 3;
constexpr double G = 1;
constexpr std::array<double, 4> K = {1, 1 / 2, 1 / 2, 1};

// Class Difinitions
// Class star
class star
{
public:  // members
    double m;
    std::array<double, DIM> x;
    std::array<double, DIM> p;
    std::array<std::array<double, DIM>, 5> kx;
    std::array<std::array<double, DIM>, 5> kp;
    int flag = 0;

public:  // constructors
    star();
    star(double input, ...);
    star(bool rand_initialization);

public:  // class functions
    void Show();
};

// Class TBP for calculate and data-gen
class TBP
{
public:  // members
    star stars[NUMBER_OF_STAR];
    float dt = 0.0001;
    std::fstream files[NUMBER_OF_STAR];

public:  // constructor
    TBP(star stars[]);

public:  // class functions
    void runge();
    void Save();
    void file_open();
    void file_close();
    void Show();
};

double Rand_0to1();
