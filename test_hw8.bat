cls

echo off

echo. >> capture.txt
echo. >> capture.txt
echo Beginning combineSamples tests > capture.txt
echo. >> capture.txt
python test_combineSamples.py >> capture.txt 2>&1

echo. >> capture.txt
echo. >> capture.txt
echo Beginning reformatSamples tests >> capture.txt
echo. >> capture.txt
python test_reformatSamples.py >> capture.txt 2>&1

echo. >> capture.txt
echo. >> capture.txt
echo Beginning extractCoordinates tests >> capture.txt
echo. >> capture.txt
python test_extractCoordinates.py >> capture.txt 2>&1

echo. >> capture.txt
echo. >> capture.txt
echo Beginning analyzeWords tests >> capture.txt
echo. >> capture.txt
python test_analyzeWords.py >> capture.txt 2>&1

echo. >> capture.txt
echo. >> capture.txt
echo *********************** All Tests Complete *********************** >> capture.txt





echo on
