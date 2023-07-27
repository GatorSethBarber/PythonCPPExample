#include <string>
#include <vector>
#include <pybind11/pybind11.h>

using namespace std;

namespace py = pybind11;

void sayHello(string name);
py::tuple createTuple(string inOne, float inTwo);

class VecWrap {
private:
        int myVar;
        vector<int> myVec;
public:
    VecWrap();

    void addNum(int num);
    void printVec();
    vector<int> gradProduct(const vector<int>& input);

    int& getMyVar();
    void setMyVar(int newVal);

};