#create an array with sorted folder names
array=($(ls -d */ | cut -f1 -d'/' | sort -f))
declare -i y=0
#Enter the directory of the git repo's
path="PATH"
#Output file name
Out="outputs1.csv"
#Name of the source code file
Filename="CODEFILE_NAME.cpp/c"
#dirname=$(ls | sort -f)
> $Out
echo Inprogress....
for dir in "${array[@]}"; 
do 
cd ${array[y]};
echo ${array[y]}
g++ $Filename
echo ${array[y]}, $"\""$(./a.out)$"\"," >> $path$Out
cd ..
y=y+1
done
echo Completed!