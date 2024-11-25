cls

echo off
echo Beginning bbanalyze tests > capture.txt
echo. >> capture.txt
python test_bbanalyze.py >> capture.txt 2>&1

echo. >> capture.txt
echo. >> capture.txt
echo *********************** All Tests Complete *********************** >> capture.txt





echo on
