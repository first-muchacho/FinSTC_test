# FinSTC_test
Test task to the company FinSTC Software LLC
## First task

Please complite XSLT test task (see description below).

А. Необходимо сделать xslt-файл для трансформации test.xml.  
B. Результат трансформации должен содержать отфильтрованные accountTransaction ноды, то есть оставить только те accountTransaction узлы, которые:
 - имеют ноду updateDate со значением 2012-12-12;
 - значение ноды spValue начинается на BT.

### Result

To deploy a project:  
1. download this repository for yoursel  
2. create and deploy a virtual environment  
3. then run the main

How it works:  
To complete the task, a python script has been written that is based on the "etree" module. The script takes the initial file (test.xml), which contains the input data. After that, an xslt file (change.xslt) opens with which the initial file will be converted. The result of the conversion is written to the output file (result.xml).
