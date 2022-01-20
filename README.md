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
3. run the main

How it works:  
To complete the task, a python script has been written that is based on the "etree" module. The script takes the initial file (test.xml), which contains the input data. After that, an xslt file (change.xslt) opens with which the initial file will be converted. The result of the conversion is written to the output file (result.xml).

## Second task

Please explain what is XSD, show examples of financial XSD.

### Result

XSD is a language for description the structure of XML document. It is also called XML Schema.
W3C (World Wide Web Consortium) recommendation this specifies how to formally describe the elements in XML document.
When using XML Schema, the XML parser can check noy only correctness of the syntax of an XML doc, but also its structure,
content model and data types.
This approach allows OOL to easily create objects in memory, which is much more easier than parsing XML as a regular text doc.
Also XSD  extensible and allows to connect ready dictionary to describe typical tasks.
XSD also has built-in documentation tools, which allows u to create independent doc that do not require additional description.

Example URL: https://cbr.ru/StaticHtml/File/92172/ValCurs.xsd

## Third task

Please find information about ETL and explain in your words where and how you would use it.
 
### Result

ETL is an abbreviation of Extract, Transform, Load. This is a system that is used to lead to the same directories and upload data from several different accounting systems to DWH and EPM.
The problem that made it necessary to use ETL solutions is the business needs to obtain reliable reporting from the mess that is going on in the data of any ERP system.
There are two kinds of this mess:  
1\. As random errors that occurred at the level of input, data transfer, or due to bugs;  
2\. As differences in directories and data details between adjacent IT systems.  

Ideally, ETL should solve the following two tasks:  
1\. To bring all data to a single system of values and details, simultaneously ensuring their quality and reliability;  
2\. To provide an audit trail during the transformation of data, so that after the transformation it was possible to understand from which source data and amounts each line of the transformed data was collected.
