#!/bin/bash
# print "Hello World!" to the bash shell in the terminal emulator 
echo -e "Hello World!\n"
#test array
testArr=( 1 2 3 4 "here we go" );
for i in "${testArr[@]}";
do
	echo $i;
done;
echo -e "\nTest Result:";
man -k ls | grep ^ls\\s;
echo -e "\nTest 2 looping through commands:";
commands=( "ls" "grep");

for i in "${commands[@]}";
do
	man -k $i | grep "^$i\\s";
done;	

