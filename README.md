# Prefixer/Suffixer

## Description

 This convenient script helps you remove prefixes or suffixes from a number of files. It can also add desired prefixes/suffixes.
 Running the script will apply the operations for all files in a given directory.
 
## Getting Started

### Executing the program

  To execute the script, run ```prefixer-suffixer.py``` with Python. Executing the script with no additional parameters will print the usage of the script.

```
python3 prefixer-suffixer.py
```



#### Parameters:

* Particle (required): The prefix/suffix text you want to remove/add.
* Directory (optional): Directory of the folder you want to apply the operations to. Default value is "." (the current working directory).
* Prefix/suffix (optional): Specifying if you want to deal with prefixes or suffixes. Default value is "prefix".
* Additive (optional): Specifying if you want to add the particle as a suffix/prefix instead of removing it. It will be false if "additive" is not given as 4th parameter.


Usage:
``` 
python prefixer-suffixer.py particle [directory] [prefix/suffix] [additive]
```

Example usage:
```
python prefixer-suffixer.py "Unwanted Suffix" "folder_path/nested_folder" suffix
```