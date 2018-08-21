# Welcome

Tag remover is a way to remove tags from file names in given directories

This is mainly used to clean up files that have similar tags on all of the file names

Anyway setup a config file like this:
```
# ROOT Directory to look through
# Comma separated list of subdirectories to crawl through
# Episode regex i.e. \((\d+)\) for an episode number inside parens. put false to ignore episode numbers
# Season number. put false to ignore season number and episodes
# a single regex tag to remove i.e. \[([a-zA-Z0-9\s]*)\] removes all tags in brackets
# a list of other tags separated by new lines
# [weird tag]
# (other tag)
# xxxXXXxxx
```

Easy Peasy

# RUNNING
**WARNING: THIS CANNOT BE REVERSED**

Assming this is your folder structure
```
TopLevel
|-config.txt
|-TagRemover.py
|-TargetFolder
| |-Sub Dir 1
| | |-Files
| |-Sub Dir 2
| | |-Files
...
```
And assuming you have the config.txt file configured properly run the command 
`python3 TagRemover.py`
Any files that cannot be relabeled with seasons/episodes will be printed to the console.
This is caused by having 2 or more numbers valid for the episode number
