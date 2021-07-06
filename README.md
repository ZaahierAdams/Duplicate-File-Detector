# Duplicate File detector 
This is a python console application for detecting and deleteing duplicate files in a directory 

## Overview 
- It detects files on the basis of **file name** and **file size** i.e. Identifies a file as a duplicate if another file has an identical name and size to a file of interest
- The application crawls through all subdirectories of the specified directory 
- By default the application deletes the duplicate file automatically 
- Once the application is runs to completion it will provide information on:
	- Number of files scanned 
	- Number of duplicates found
	- Number of remaining files after scan
	- Size of files deleted in megabytes
	- Time taken to complete scan  

## Getting Started
- Change the directory of interest in `Duplicate_det.py`
```
direct = 'C:\\DIRECTORY_HERE'
```

- Change the file extension in `Duplicate_det.py`. This is the type of files you're interested in scanning. Accepts only one file type. For example `ftype=.jpg`. Ensure that the the file extension the preceded by a dot (.)
```
ftype = '.FILE_TPYPE'
```

- Run the application in your IDE


