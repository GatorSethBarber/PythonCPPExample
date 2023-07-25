#include <pybind11/pybind11.h>
#include "example.hpp"

// See https://www.youtube.com/watch?v=_5T70cAXDJ0 for structure and explanation

namespace py = pybind11;

PYBIND11_MODULE(example, handle) {
    handle.doc() = "Hello, world!";
    handle.def("say_hello", &sayHello);

    py::class_<VecWrap> (
        handle, "PyClassName"
        )
        .def(py::init<>())
        .def("add_num", &VecWrap::addNum)
        .def("print_vec", &VecWrap::printVec)
    ;
}