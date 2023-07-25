# include <string>
#include <vector>

using namespace std;

void sayHello(string name);

class VecWrap {
private:
        vector<int> myVec;
public:
    VecWrap();

    void addNum(int num);
    void printVec();

};