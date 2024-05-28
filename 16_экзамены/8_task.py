# Напишите программу, которая обходит все файлы в директории, переданной ей как параметр и выводит на экран имена тех, чей размер задан как второй параметр. Реализовать рекурсивный обход поддиректорий.

#!/bin/bash

# if [ $# -ne 2 ]; then
#     echo "Usage: $0 <directory> <size>"
#     exit 1
# fi

# if [ ! -d "$1" ]; then
#     echo "Error: '$1' is not a directory."
#     exit 1
# fi

# directory=$(realpath "$1")

# size=$2

# files=$(find "$directory" -type f -size "${size}c")

# if [ -z "$files" ]; then
#     echo "No files found with size ${size} bytes in directory $directory."
#     exit 0
# fi

# echo "$files"
