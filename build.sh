as $1.s -o $1.o
ld -macosx_version_min 13.0 -o $1 $1.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -arch arm64 -e _start
./$1

rm $1.o