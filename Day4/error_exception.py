#Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:



#Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal


#Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError.

#The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).



#Handling Exceptions

#It is possible to write programs that handle selected exceptions
#note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.

#A try statement may have more than one except clause, to specify handlers for different exceptions.

#At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:


# while True:
#     try:
#         num=int(input("Enter any integer :"))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


#A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class).


# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


#Note that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.


# import sys

# try:
#     f = open('file.py')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


#The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

#The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

# def devide(x,y):
#     try:
#         result=x/y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")

# devide(9,8)

#finally clause is executed in any event. The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.


#The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances.


# class Error(Exception):
#     """Base class for exceptions in this module."""
#     pass

# class InputError(Error):
#     """Exception raised for errors in the input.

#     Attributes:
#         expression -- input expression in which the error occurred
#         message -- explanation of the error
#     """

#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message

# class TransitionError(Error):
#     """Raised when an operation attempts a state transition that's not
#     allowed.

#     Attributes:
#         previous -- state at beginning of transition
#         next -- attempted new state
#         message -- explanation of why the specific transition is not allowed
#     """

#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message



# while True:
#     try:
#         x=int(input("Enter the integer:"))
        
#     except ValueError:
#         print("This is not valid integer")
#     except Exception:
#         print("Something went wrong.!")
#     finally:
#         print("Done")


####

# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass


# # you need to guess this number
# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")
        
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")

  


# try:
#   print(x)

# except TypeError:
  

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")






def check_num():
   try:
      number=int(input("Enter any number :"))
      if number > 0:
         return "Positive"
      elif number < 0:
         return "Negative"
      else:
         raise ValueError("Number is zero")
   except ValueError as e:
      return str(e)

print(check_num()) # Positive




def check_even_odd(number):
   try:
      if number % 2 == 0:
         raise ValueError("Number is even")
      else:
         raise ValueError("Number is odd")
   except ValueError as e:
      return str(e)

print(check_even_odd(5)) # Number is odd
print(check_even_odd(4)) # Number is even









try:
   # some code here
   # that might raise a SyntaxError
   eval("1 +") # this will raise a SyntaxError
   a=10/0
except SyntaxError as e:
   # handle the SyntaxError exception
   # e is the exception instance
   print(f"Caught a SyntaxError: {e}")
except ZeroDivisionError:
   print("Zero")



try:
   # some code here
   # that might raise a SyntaxError or ZeroDivisionError
   eval("1 +") # this will raise a SyntaxError
   10 / 0 # this will raise a ZeroDivisionError
except SyntaxError as e:
   # handle the SyntaxError exception
   # e is the exception instance
   print(f"Caught a SyntaxError: {e}")
except ZeroDivisionError as e:
   # handle the ZeroDivisionError exception
   # e is the exception instance
   print(f"Caught a ZeroDivisionError: {e}")




class CustomError(Exception):
   """Custom exception class for our custom error handling program."""
   def __init__(self, message):
      self.message = message

def some_function():
   # some code here that might raise our custom error
   raise CustomError("This is a custom error message")

try:
   some_function()
except CustomError as e:
   # handle the custom error
   print(f"Caught a CustomError: {e}")

