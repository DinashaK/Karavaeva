# Сценарий должен имитировать работу лототрона -- извлекать 5 случайных неповторяющихся чисел в диапазоне 1 - 50. Сценарий должен предусматривать как вывод на stdout, так и запись чисел в файл, кроме того, вместе с числами должны выводиться дата и время генерации данного набора.

#!/bin/bash

# entries=$(shuf -i 1-50 -n 5 | tr '\n' ' ')

# TIME=$(date '+%H:%M:%S')
# DATE=$(date '+%d/%m/%Y')

# RESULT="$DATE $TIME -> $entries"

# if [ "$1" = "-f" ]; then
#     if [ -z "$2" ]; then
#         echo "Ошибка: При использовании флага -f необходимо передать название файла!" >&2
#         exit 1
#     fi
#     echo "$RESULT" >> "$2"
# else
#     echo "$RESULT"
# fi
