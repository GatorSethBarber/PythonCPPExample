#include "example.hpp"
#include <iostream>

using namespace std;
void sayHello(string name) {
    cout << "Hello, " << name << "." << endl;
}

VecWrap::VecWrap() : myVec() {}

void VecWrap::addNum(int num) {
    myVec.push_back(num);
}

void VecWrap::printVec() {
    cout << "<";
    for (int& i : myVec)
        cout << i << " ";
    cout << ">" << endl;
}