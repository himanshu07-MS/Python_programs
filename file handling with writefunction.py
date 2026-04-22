# file handling with write function

fileptr = open('himanshu.txt','w');

content = fileptr.write('Alphabet');            # store data

print(type(content))                         # refers data type
print(content)                                  # print the content of file


fileptr.close()                                  # close the apend file.

