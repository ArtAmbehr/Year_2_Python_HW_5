# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def file_info(path):
    # Разделяем абсолютный путь файла на его директорию и на имя:
    dirname, filename = os.path.split(path)
    
    # Разделяем имя файла с расширением - на имя и расширение:
    filename, file_extension = os.path.splitext(filename)
    
    return (dirname, filename, file_extension)

path = '/Users/user/Documents/example.txt'
result = file_info(path)
print(result)
