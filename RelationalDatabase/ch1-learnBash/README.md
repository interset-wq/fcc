# Learn Bash by Building a Boilerplate

## Abstract

The terminal allows you to send text commands to your computer that can manipulate the file system, run programs, automate tasks, and much more.

In this 170-lesson course, you will learn terminal commands by creating a website boilerplate using only the command line.

## Note 

### pwd

print work directory path

### ls

like `dir` in Windows, list

You can add a `flag` to a command to use it different ways like this: `ls <flag>`. List the contents of the node_modules folder in "long list format". Do that by adding the `-l` flag to the "list" (`ls`) command.

`ls -l` show detailed info of files

### cd

change directory

> [!NOTE]
> folder and directory are the same thing

`cd ..` back to one level

`cd ../..` go back 2 folders

### more

see what's in a file with `more <filename>`

### clear

clear the terminal

### mkdir

make directory

make a new folder with `mkdir <folder_name>`

`mkdir folder/<new_folder_name>`

### echo

like `print()` of Python, without `""`

The `echo` command lets you print anything to the terminal. You used it in the first lesson. Just type what you want to print after it. Use it to print hello website to the terminal.

You can print to a file instead of the terminal with `echo text >> filename`. 

### touch

You can use `touch <filename>` to create a new file

### --help

Most commands have a `--help` flag to show what the command can do. Display the "help" menu for the ls command. Here's an example: `command <flag>`

`ls -a` don't hide files, such as `.gitignore`

### `.` & `..`

The `.` takes you to the folder you are in, and `..` takes you back, or up, a folder.

### cp

You can copy a file with `cp <file> <destination>`. cp stands for "copy".

### rm

You can remove a file with `rm <filename>`. 

`rm -r <directory_name>` remove the folder and the files in it

> [!WARNING]
> You should be very careful when recursively removing files like that. It will delete everything, and can destroy your operating system.

### mv

You can rename them with `mv` like this: `mv <filename> <new_filename>`. `mv` stands for "move", it can rename or move something. 

`mv <file> <destination>` move file

### find

You can use `find` to find things or view a file tree.

You can use `find <folder_name>` to display the tree of a different folder.

`find -name <filename or folder>` It shows you where that file is.

### rmdir

You can use `rmdir <directory_name>` to remove a folder. rmdir stands for "remove directory". 

### exit

exit terminal