#!/bin/bash

workingDirectory=$(dirname $0)
year=2021
output="part1.py"

for i in {1..30..1} 
do
	day="$workingDirectory/$year/day$i"
	mkdir $day
	touch $day/$output
	
	python $workingDirectory/pythonTemplateCreator.py 2 $day/$output
done
