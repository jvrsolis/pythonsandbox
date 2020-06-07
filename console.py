from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Punctuation, Literal, Other, Text
from pprint import pformat
from termcolor import colored, cprint
import termtables


class ConsoleStyle(Style):
    styles = {
        Comment:                'italic #828',
        Keyword:                'bold #FF6CC9',
        Name:                   '#00B1DC',
        Name.Function:          '#00FF68',
        Name.Class:             '#50B3C2',
        Literal:                'bold #FF8000',
        String:                 'bold #00FF68',
        Number:                 'bold #00B1DC',
        Punctuation:            'bold #FF8000',
    }


class Console:
    @staticmethod
    def info(string):
        cprint(string, 'green')

    @staticmethod
    def error(string):
        cprint(string, 'white', 'on_red')

    @staticmethod
    def comment(string):
        cprint(string, 'yellow')

    @staticmethod
    def warn(string):
        cprint(string, 'grey', 'on_yellow')

    @staticmethod
    def question(string):
        cprint(string, 'grey', 'on_cyan')

    @staticmethod
    def notice(string):
        length = len(string) + 12
        Console.info("*" * length)
        Console.info("*     " + string + "     *")
        Console.info("*" * length)

    @staticmethod
    def success(string):
        cprint(string, 'grey', 'on_green')

    @staticmethod
    def alert(string):
        length = len(string) + 12
        Console.comment("*" * length)
        Console.comment("*     " + string + "     *")
        Console.comment("*" * length)

    @staticmethod
    def table(string):
        string = termtables.to_string(
            [["Alice", 24], ["Bob", 19]],
            header=["Name", "Age"],
            style=termtables.styles.ascii_thin_double,
        )
        Console.output(string)

    @staticmethod
    def output(code):
        print(highlight(pformat(code),
                        PythonLexer(), Terminal256Formatter(style=ConsoleStyle)))
