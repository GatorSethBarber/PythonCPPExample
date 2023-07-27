Rem for comments: https://www.tutorialspoint.com/batch_script/batch_script_comments.htm
Rem for user input: https://www.geeksforgeeks.org/batch-script-input-output/
Rem for conditional: https://stackoverflow.com/questions/5591491/conditional-statements-in-batch-files
Rem for MSBuild release option: https://docs.revenera.com/installshield22helplib/helplibrary/MSBuild_CmdLine.htm

set /p input= "Run cmake [y/n]: "
if "%input%"=="y" (
    echo "Running cmake"
    cmake -S . -B build
)
cd build
MSBuild testingSwig.sln /property:Configuration=Release
copy .\Release\*.pyd ..\
echo "Testing"
cd ..
python hello.py