# Написать скрипт, который выведет всех потомков процесса по его PID.

#!/bin/bash

# if [[ $# -ne 1 ]]; then
#     echo "Ошибка: не задан PID процесса" >&2
#     exit 1
# fi

# PROCNAME=$(ps -o comm= -p $1)
# echo "Потомки процесса $PROCNAME с PID $1:"

# pstree -p $1