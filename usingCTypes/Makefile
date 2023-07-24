#See https://www.youtube.com/watch?v=b1E-4EZJ9OU for code
#For using -shared, see Makefile in usingSwig

mingw_includes = C:\mingw\mingw64

standard:
	g++ -shared -o sample.dll sample.cpp -fPIC -I$(mingw_includes)
	python test.py