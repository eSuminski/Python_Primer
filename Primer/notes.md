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

### Key words

#### control flow
```Python
for # used if you want something to loop
in # use this when you want to reference something inside another element
while # use this when you want to loop for specified conidtion
```

#### exceptions
```Python
try # this is used to start your try except block. Use this when you think something can go wrong
except # use this to handle things going wrong
finally # use this when you need something to happen whether your code executes successfully or not
raise # use this to raise an exception
```

#### importing
```Python
from # use this to specify where you are importing your code from
import # use this to import your code
as # you can set a reference to whatever it is you are importing
```

#### logical operators
```Python
is # use this when you want a True result when A = B
is not # use this when you want a True result when A != B
and # use this when you want to set up multiple trigger conditions
or # use this when you want to set up multiple optional trigger conditiona
if # use this when you want code to run under specified conditions
elif # use this when you want code to run under conditions not covered by the if statement
else # use this to run code if your if and elif statements do not run
True # boolean indicating something is true
False # boolean indicating something is false
```

#### others

```Python
None # default function return value
pass # use this to ignore code
def # used to create functions
class # used to create classes
assert # used for testing to get a boolean result
break # used to escape a loop
```

#### operators
```Python
+ # addition
- # subtraction
* # multiplication
/ # division
** # power of
% # modulus
// # floor division
```

### Python Scopes
Python follows LEGB scopping 
Local: this is available in the local code block (current indenting)
Enclosing: this is available to any code within the code block including inner blocks (functions in functions)
Global: this is available to all code within the module
Built-in: these are the key words and method signatures provided by Python. Do not repurpose these

### Python Classes
```Python
class ClassName(Extended, Classes):
    def __init__(self, parameters, go, here="this is a default value, must go at end"):
        self.parameters = parameters
        self.go = go
        self.here = here
```

### Collections
```Python
List = [1,2,3,4]
Set = {1,2,3,4}
Tuple = (1,2,3,4)
Dictionary = {"a":1,"b":2,"c":3}
```

|Collection|Mutable|Duplicates|Indexable|
|----|-------|----------|---------|
|List| yes   | yes      | yes     |
|Set | yes   | no       | no      |
|Tuple| no   | yes      | yes     |
|dictionary| yes | no(key) | version |
