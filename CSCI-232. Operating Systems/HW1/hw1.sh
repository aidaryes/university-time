#!/bin/bash

zipFile=$1
solution=$2
contains=$3

#first task
mkdir Extract
tar xvf $zipFile -C Extract

#second task
mkdir "Exact copies"
mkdir "Referenced"
mkdir "Original"

#third task
cTotal=0

cExCopy=0
cRef=0
cOrig=0
cRatio=0

for i in Extract/*.c
	do
		cTotal=$((cTotal+1))
		if diff $i $solution >/dev/null 
		then
			cExCopy=$((cExCopy+1))
			mv $i "Exact copies"
		elif grep -q $contains $i
		then
			cRef=$((cRef+1))
			mv $i "Referenced"
		else
			cOrig=$((cOrig+1))
			mv $i "Original"
		fi
done

cRatio=$(bc <<< "scale=4;$cOrig/$cTotal")

touch "report.txt"

echo "Exact copies $cExCopy" >> "report.txt"
echo "Referenced $cRef" >> "report.txt"
echo "Original $cOrig" >> "report.txt"
echo "Ratio 0$cRatio" >> "report.txt"

now=$(date +"%m_%d_%Y")
nameZip="result-$now"
tar cvzf $nameZip.tar.gz report.txt $solution "Exact copies" "Referenced" "Original"

rm -rf "Exact copies" "Referenced" "Original" "Extract" $zipFile $solution "report.txt"


