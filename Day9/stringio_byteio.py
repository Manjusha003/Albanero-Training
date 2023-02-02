# The StringIO module is an in-memory file-like object. This object can be used as input or output to the most function that would expect a standard file object. When the StringIO object is created it is initialized by passing a string to the constructor. 
# If no string is passed the StringIO will start empty. In both cases, the initial cursor on the file starts at zero.

# to work with this module we have to import it from the io module in Python as io.StringIO.
# from io import StringIO

# string ='This is initial string.' 
# # Using the StringIO method to set as file object. Now we have an object file that we will able to treat just like a file.
# file = StringIO(string)

# # this will read the file
# print(file.read())

# file.write("Welcome to python tutorial")
# file.seek(0)
# # print(file.read())

# #  StringIO.getvalue(): This function returns the entire content of the file.
# print(file.getvalue())

# # StringIO.isatty():This function Return True if the stream is interactive and False if the stream not is interactive
# print(file.isatty())

# # StringIO.readable():This function return True if the file is readable and returns False if file is not readable.
# print(file.readable())

# # StringIO.writable():This function return True if the file supports writing and returns False if file does not support writing.
# print(file.writable())

# # StringIO.seekable():This function return True if the file supports random access and returns False if file does not support random access.
# print(file.seekable())

# # StringIO.closed:This function return True if the file is closed and returns False if file is open.
# print(file.closed)

#StringIO.truncate(): This function is used to resize the size of the file stream. This method drops the file after the provided index and saves it.


# Importing the StringIO module.
# from io import StringIO


# # The arbitrary string.
# string ='Hello and welcome to GeeksForGeeks.'

# # Using the StringIO method
# # to set as file object.
# file1 = StringIO(string)

# # Reading the file:
# print(file1.read())

# Now if we again want to read
# the file it shows empty file
# because the cursor is set to
# the last index.


# This does not print anything
# because the function returns an
# empty string.
# print(file1.read())

# Hence to set the cursor position
# to read or write the file again
# we use seek().We can pass any index
# here from(0 to len(file))
# file1.seek(0)
# file1.truncate(10)
# Now we can able to read the file again()
# print(file1.read())

# StringIO.tell(): This method is used to tell the current stream or cursor position of the file.

# str="hello friends"

# file2=StringIO(str)
# print(file2.read())
# file2.seek(0)
# print(file2.tell())
# file2.seek(7)
# print(file2.tell())

# file2.close()
# print(file2.closed)



# BytesIO implements read and write bytes data in memory. We create a BytesIO object and then write some bytes data into it. Please note that instead of writing a string, you write utf-8 encoded bytes with the BytesIO object.


from io import BytesIO

bytio=BytesIO()
bytio.write("hello".encode('utf-8'))
print(bytio.getvalue())
print(bytio.read())



import io

# Convert a StringIO object to BytesIO object.
def stringio_to_bytesio(str):
    
    str_io_object = io.StringIO(str)
    
    str_data = str_io_object.read().encode('utf8')
    
    bytes_io_object = io.BytesIO(str_data)
    
    print(bytes_io_object)  

    print(bytes_io_object.read())
    

# Use io.TextIOWrapper to convert BytesIO object to a string. Then we can build a StringIO object on the string.     
def bytesio_to_stringio(bytes_str):
    
    data = io.BytesIO(bytes_str)
    
    # Create an instance of io.TextIOWrapper class.
    text_wrapper = io.TextIOWrapper(data, encoding='utf-8')
    
    str = text_wrapper.read()
    
    str_io_object = io.StringIO(str)

    print(str_io_object)  
    
    print(str)  

if __name__ == '__main__':
    
    bytes_str = stringio_to_bytesio('I love python')
    
    bytesio_to_stringio(b'hello python')
