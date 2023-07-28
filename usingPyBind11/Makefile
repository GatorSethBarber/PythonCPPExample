# For compilation statement: https://stackoverflow.com/questions/60699002/how-can-i-build-manually-c-extension-with-mingw-w64-python-and-pybind11
# Official compilation resource: https://pybind11.readthedocs.io/en/stable/compiling.html
# For tutorial: https://www.youtube.com/watch?v=_5T70cAXDJ0
# Official documentation to get pybind11: https://pybind11.readthedocs.io/en/stable/installing.html

python_loc = C:\Users\coder\AppData\Local\Programs\Python\Python311
python_lib = python311
python_version = 3.11

standard:
	echo "If error, use the following as the suffix"
	py -$(python_version) -c "from distutils import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))
	g++ -shared -o example.cp311-win_amd64.pyd example.cpp pybinds.cpp -I../extern/pybind11/include/ -I$(python_loc)\include -L$(python_loc)\libs -l$(python_lib)
	py -$(python_version) test.py test