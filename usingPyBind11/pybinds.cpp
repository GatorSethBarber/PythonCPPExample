#include <pybind11/pybind11.h>    // main header
#include <pybind11/stl.h>         // For standard (possibly inefficient) type conversions
#include <pybind11/numpy.h>       // For numpy
#include "example.hpp"

// See https://www.youtube.com/watch?v=_5T70cAXDJ0 for structure and explanation

namespace py = pybind11;

PYBIND11_MODULE(example, handle) {
    handle.doc() = "Hello, world!";
    handle.def("say_hello", &sayHello);
    // One implementation of getting c++ to work with python
    handle.def("create_tuple", &createTuple);
    handle.def("make_triplet", [](int argOne, string argTwo) {
        return py::make_tuple(argOne, argTwo, argTwo + to_string(argOne));
    });

    py::class_<VecWrap> (
        handle, "PyClassName"
        )
        .def(py::init<>())
        .def("add_num", &VecWrap::addNum)
        .def("print_vec", &VecWrap::printVec)
        .def("grad_product", &VecWrap::gradProduct)
        .def("g_prod_numpy", [](VecWrap& self, const py::array_t<int>& input){
            py::array_t<int> output = input;
            output = output.reshape({-1});
            for (int i = 1; i < output.shape(0); i++)
                output.mutable_at(i) *= output.at(i - 1);
            return output;
        })
        .def_property("my_var", &VecWrap::getMyVar, &VecWrap::setMyVar)
    ;
}