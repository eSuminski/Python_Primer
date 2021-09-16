import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

def print_hello():
    print("hello!")

logging.debug("calling print_hello()")
print_hello()
logging.warning("print_hello() has finished")

# debug
# info
# warning
# error
# critical