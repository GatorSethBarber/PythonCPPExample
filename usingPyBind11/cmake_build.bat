cd build
cmake ../..
MSBuild example.sln
cd Debug
copy *.pyd ..\..
cd ../..
python test.py