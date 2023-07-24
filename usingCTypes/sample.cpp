#include "sample.hpp"

using namespace std;


bool divizByTwo(int integer) {
    return integer % 2 == 0;
}

void printInput(char* input) {
    string newInput = input;
    cout << "Input: " << newInput << "; end input" << endl;
}