# include "example.hpp"

using namespace std;

int timesTwo(int input) {
    return input * 2;
}

void echoPrint(string input) {
    cout << "Input: " << input << endl;
}


void IncPrint::printAndInc() {
    cout << "Counter: " << ctr++ << endl;
}

void IncPrint::overloaded(int hello) {
    cout << "Called with int " << hello << endl;
}

void IncPrint::overloaded(string hello) {
    cout << "Called with string " << hello << endl;
}