#See https://www.youtube.com/watch?v=b1E-4EZJ9OU for code
#For using -shared, see Makefile in usingSwig
# For getting include path for python: Answer by Robᵩ in https://stackoverflow.com/questions/35071192/how-to-find-out-where-the-python-include-directory-is

standard:
	g++ -shared -o sample.so sample.cpp -fPIC $$(python3-config --includes)
	python3 testLinux.py