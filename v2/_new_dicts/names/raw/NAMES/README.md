this is a pool of name files and a python function that combines all their content into one file to be used in the program.

the python script exectures the following operations in the same order

pull name from all files with a name of schema "names_" + something + ".txt"

> lower case each name
> if a [space] is part of the name:
	make verions of the name in all combinations (normal, without space(s), each part individually)
> merge all file sets, uniqify
> output a file of schema "_names_" + date + ".txt" 


to add new names:
> put them into a file of schema 1. 
> put this file into this folder
> run the python script
> take the file of schema 2 with the latest date.
