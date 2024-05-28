# Напишите программу, которая копирует файл с удаленного хоста в текущую папку по SSH. Имя файла и адрес хоста принимать как параметры.

#!/bin/bash

# if [ $# -ne 2 ]; then
#     echo "Usage: $0 <filename> <remote_host>"
#     exit 1
# fi

# filename=$1
# remote_host=$2

# rsync -avz --progress "$remote_host:$filename" .

# if [ $? -eq 0 ]; then
#     echo "File '$filename' copied successfully from $remote_host."
# else
#     echo "Error: Failed to copy file '$filename' from $remote_host."
# fi

