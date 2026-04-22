# file handling with read function

fileptr = open('himanshu.txt','r');

content = fileptr.read(100);            # store data

print(type(content))                         # refers data type
print(content)                                  # print the content of file


fileptr.close()                                  # close the apend file.
