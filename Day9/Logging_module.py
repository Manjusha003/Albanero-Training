# logging is useful to track the error or excepation or information
# it helps in debugging.


# import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This will get logged")


# from logging import *

# basicConfig(
#     filename='app.log',
#     filemode='w',
#     format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s ',
#     level=DEBUG
# )
# warning("This will get logged to the file")



# warning("This is warning")
# critical("this is critical")
# debug("this is debug")
# error("this is error")
# info("this is info")




# from logging import *

# basicConfig(
#     filename='app.log',
#     format=' {asctime} - {name} - {levelname} - {message}',
#     style='{'

# )
# warning("This will get logged to the file")



from logging import *
basicConfig(
    filename='app.log',
    format='{name} -- {asctime} -- {message}',
    style='{'
)

logger=getLogger("Main")
logger.warning("Warning is coming..")
logger.debug("It is debugging...")
logger.error("Error occured")
