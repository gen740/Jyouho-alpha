#pragma once
#include <array>
#include <fstream>

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

public:
    void Show();
};

class TBP
{
public:  // members
    star stars[NUMBER_OF_STAR];
    float dt = 0.0001;
    std::fstream files[NUMBER_OF_STAR];

public:  // constructor
    TBP(star stars[]);
    ~TBP();

public:  // class functions
    void runge();
    void Save();
    void Show();
};
