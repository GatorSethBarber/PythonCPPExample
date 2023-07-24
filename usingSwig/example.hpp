#pragma once
#include <string>
#include <iostream>

using namespace std;

int timesTwo(int input);
void echoPrint(string input);

class IncPrint {
    int ctr = 0;
    public:
        void printAndInc();
        void overloaded(int hello);
        void overloaded(string hello);
};