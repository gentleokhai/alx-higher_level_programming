#!/bin/bash
find . -name "*.c"
for file in $(find . -name "*.c"); do
    gcc -c -o ${file%.c}.o $file
done
gcc -shared -o liball.so *.o
rm *o
