import sys
from traceback import format_exception
from console import Console


def exception_handler(exctype, value, traceback):
    Console.error("FATAL ERROR - " +
                  "".join(format_exception(exctype, value, traceback)).strip())
    sys.exit(0)


sys.excepthook = exception_handler
