#include "example.hpp"
#include <iostream>

using namespace std;
void sayHello(string name) {
    cout << "Hello, " << name << "." << endl;
}

py::tuple createTuple(string inOne, float inTwo) {
    return py::make_tuple(inOne, inTwo);
}

VecWrap::VecWrap() : myVec(), myVar(7) {}

void VecWrap::addNum(int num) {
    myVec.push_back(num);
}

void VecWrap::printVec() {
    cout << "<";
    for (int& i : myVec)
        cout << i << " ";
    cout << ">" << endl;
}

vector<int> VecWrap::gradProduct(const vector<int>& input) {
    vector<int> copy(input.size());
    copy[0] = input[0];
    for (int i = 1; i < copy.size(); i++)
        copy[i] = input[i] * copy[i - 1];
    return copy;
}

int& VecWrap::getMyVar() {
    cout << "Getting my var" << endl;
    return myVar;
}
void VecWrap::setMyVar(int newVal) {
    cout << "Setting my var to " << newVal << endl;
    myVar = newVal;
}