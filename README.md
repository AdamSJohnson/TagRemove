**Welcome**

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
