# Python Notes

### Compiler and Interpreter
A compiled language uses a compiler to take the entirety of your source code and creates an executable file. Compilation time can be longer because everything must be compiled, but it ultimately allows for faster applications 

Intepreters take the entirety of your source code, pre-compiled code, and scripts, and executes them for you. More memory intensive, but also more flexible: can easily run snippets of code without a lot of code overhead.

### Pip
Pip is your package manager. All you have to do is type "pip install (whatever you want to download)"

### Pypi
Pypi is the main repository off all python packages

### Naming Conventions
for packages, python files (modules), variables, and functions:
- use snake_case

for classes and exceptions
- use PascalCase

for constants
- use SCREAMING_SNAKE_CASE


### Python
Python is a dynamically typed language.
- Python handles type assignment for you
- data types
    - EVERYTHING IS AN OBJECT
- Numeric types:
    - int
    - float
    - complex
- String
    - no char
- Boolean
    - True
    - False
- None

Python is a strongly typed language
- Python will not coerce types for you

Python utilizes "Just in Time" compiliation
- what this means is Python goes line by line compiling and executing code

Python is a high level language
- automates memory management for you
- handles garbage collection for you
- developers don't use pointers

### REPL
stands for:
READ: python can take input
EVALUATE: python can perform functions
PRINT: Python can return a result to you
LOOP: Python can continue to do these steps
- remember, this is all done in a terminal: no IDE necessary
- HOWEVER! Information is not persisted beyond the session
    - Use an IDE if you want to create a Python app
- enter python in a terminal to start
- use ctr + z or exit() to exit

### Pylint
Pylint is used for static code analysis. It helps you to create readable code that follows standard conventions and it can oftentimes find errors in your code
commands:
- pylint package\module
- pylint package

### unit test basic
format:
```python 
def test_name_of_test():
    # the test itself
    assert # result of test expected
```
commands:
- pytest package (runs all tests inside the package)
- pytest package\module (runs tests inside the module)