# Python Clean Coding

When we are working on a python code, whether it is a script or a bigger project, it is only a matter of time for us to come back at it.
No matter the reason, if some time has passed, it is very likely that we won't remember as well as before what the code was supposed to do.
Keeping a coding project **maintainable** means that not only we will be able to come back at it in the future to apply fixes and new features, but also that other people can do the same.
However, there are a few guidelines to follow in order to do so.

In this module, you will learn these guidelines I recommend for keeping codes maintainable and clean coding it.

**Content**
* [Naming conventions](#naming-conventions)
  * [Variables](#variables)
  * [Functions](#functions)
  * [Classes](#classes)
* [Documenting your project](#documenting-your-project)
  * [Type hints](#type-hints)
  * [Docstrings](#docstrings)
* [Organizing your project](#organizing-your-project)
  * [Project's files](#projects-files)
  * [Easy imports](#easy-imports)

## Naming conventions

General naming conventions to follow are the ones specified at the [Google styleguide](https://google.github.io/styleguide/pyguide.html#s3.16-naming).
These following are some additions and clarifications.

### Variables

**Use meaningful names**

Variables tend to store information.
It is crucial that we know what information it stores in order to:
- Use this information whenever it is needed
- The information is not stored/estimated multiple times at different places

For example, people can be tempted to use `res` or `result` to store the information of a mathematical expression, among many other possibilities.
Let's take the following expression:

```python
res = (temp - 32) / 1800
```

It does not look so clear at first sight what the code is estimating.
If the names used for `res` and `temp` are renamed correctly, the equation is then self-explanatory.

```python
celsius = (fahrenheit - 32) / 1800
```

**Shortening names**

Using "meaningful names" also applies to avoid shortening names too much.
At the previous example, `temp` is also confusing as it is a highly used word for temporary variables.
However, in this case it is referred to `temperature`.

Shorting names in general is implemented to prevent very long lines.
Nowadays, we have wider screens and better methods to prevent this.
While there are still cases to shorten names, this is a practice to avoid.

For example, the variable `vec_st` is brief, but it might be unclear what it refers to by a quick glimpse.
Using `vector_state` is not that long and clarifies a lot the meaning.

There are still some short names that are used, like `temp` for "temporal variable" or `nof_` (prefix) for "number of --".
Feel free to use any of them or to create your own rules, as long as:
- You remain consistent with your rules.
- They do not affect any case at the understanding of the variable's content.

**Avoid single-character names**

Names like `i`, `j` or `v` tend to create many [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)).
These must be avoided, as they can turn against us in the future.<br>
Within these three named variables, `v` could refer to `velocity`, `vector`, `volume` or just anything not related to any keyword.

A clear example where these can be used is the "for-loop" that any coding teacher shows:
```python
# This loop iterates over the range of numbers [0, 10) and prints the number
for i in range(10):
    print(i)
```

While this seems like a basic example, it costs no effort to correctly name to understand better what is holds:

```python
for number in range(10):
    print(number)
```

### Functions

While following the previous naming conventions, explained for the variables, functions should be named as the operation or action to carry.

Functions might also require of given parameters.
Each parameter should be clearly named as if it was a variable.

```python
def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1800
    return celsius
```

### Classes

Python classes are a great way to keep code organized.
They are to be defined whenever you are looking for an instance that allows one or multiple of the following:
- Holding multiple types of information (mostly related).
- Providing operations on extra variables and the stored information.
- Creating a basic structure for multiple structures

**Classes** are to be named as the structure that the instance will hold.
Its **methods** follow the same naming conventions as the functions, as they are 'functions' that use information stored within the class.
Any **property** and **attribute** follow the variable's naming conventions, as they are 'variables' stored within the class.

Let's take a 'Circle' class as an example that can hold attributes and properties:

```python
import numpy as np

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        return self.__radius * 2

    @property
    def area(self):
        return self.__radius * 2 * np.pi


my_circle = Circle(3.5)
print(my_circle.radius)  # This prints 3.5
print(my_circle.diameter)  # This prints 7.0
print(my_circle.area)  # This prints 21.991148575128552
```

Note that the property `Circle.area` is actually a "function" that calculates the area of the circle.
However, due it is accessible as an attribute, it should not be named as an action, but as the value it returns.

## Documenting your project

Documenting is very important, not only to understand how the tool should behave but also what it needs in order to work.
While a user would only need a `README.md` file, keeping your code properly documented also allows them to understand if they are using anything wrong.

### Type hints

Type hints define the type of where it is being specified.
They mostly specify types for variables and parameters and return types for functions.

Specifying a **variable or parameter** is done by using `: {type}` after the name and before defining any value.

```python
number: int = 0  # 'number' is an integer

def convert_fahrenheit_to_celsius(fahrenheit: float):
    # 'Fahrenheit' is to be a float, although integers are also accepted
    celsius = (fahrenheit - 32) / 1800
    return celsius
```

**Return types** are used for specifying the type of the value(s) a function, method, or property will return.
It is specified by using `-> {type}`.

```python
def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) / 1800
    return celsius
```

For certain types, Python contains a built-in package called [`typing`](https://docs.python.org/3/library/typing.html).
It contains multiple types which are not specified in python itself, as it happens with `int` or `float`.

```python
from typing import List

def print_even_numbers(numbers: List[int]):
    # 'numbers' is a list full of integers
    for number in numbers:
        if number % 2 == 0:
            print(number)
```
Please take a deeper look into `typing`, as it won't be fully covered in this project.

Additionally, type hints also help you in the future with the auto-completion tool from your IDE.
At this last example, `numbers` is defined as a list.
Then, if we type `numbers.` our IDE should open a prompt of many options to choose, like the functions `append()` or `pop()`.

They also help to prevent mistakes.
With the same example, if someone tries to use `print_even_numbers(numbers=2)` then the IDE should complain, as '2' is an integer and not a list.


### Docstrings

Docstrings are an organized definition of a function and the parameters it needs.
While there are different types of them, I personally like [**numpy docstrings**](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) and will be using them for the examples.

You must have noticed that, in the 'type hints' section, the first line I added in the functions is a comment clarifying the parameter type.
This case is covered within docstrings.

```python
def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    This function converts the given Fahrenheit degrees into celsius.
    
    Parameters
    ----------
    fahrenheit: float
        The temperature given in Fahrenheit.
        
    Returns
    -------
    celsius: float
        The temperature in Celsius.
    """
    celsius = (fahrenheit - 32) / 1800
    return celsius
```

It might seem like redundant information specifying the types with both type hints and docstrings, but it is not.
Consider that type hints are mostly a use for the programmer using the IDE, while docstrings are the documentation the programmer can read to get informed about a class, function, property, method or any other.

## Organizing your project

### Project's files

Just like with the code, keeping a good project structure is an exceptional practice to keep your project maintainable in the future.

Taking up the [project structure](package-development.md#project-structure) specified in the 'package development' module, all code should be contained within the same folder defined as 'package_name'.
For the sake of the explanation, we will temporarily ignore any other folder in that graph.

The best way to organize your code is maintaining multiple files.
These files also follow some rules to prevent the whole project evolving into a jungle of files:

Standalone **functions** can be organized in modules, with each module specifying what contains. 
For example, it would be expected to have only math related code in a module named `math_functions.py`.<br>
Avoid having modules like `misc.py` or `func.py`, just to keep everything in a better organization.

When possible, the code should be **organized in python classes** and then, create a module per class.
Taking the previous example of a class named `Circle`, this would be expected to be stored in a module `circle.py`.<br>
While classes are named in _CamelCase_, modules should be named in _snake_case_.
If the class had been `MyCircle`, the module's name would have been `my_circle.py`

Regarding command line interface, I personally find useful creating a new module named `_cli.py`.
This contains all needed functions that are called only through the command line interface.

### Easy imports

You may have noticed this `__init__.py` file from time to time, if you have some experience in Python.
This module exists to convert a conjunction of python files into a package.
However, it also allows to easily import the package content without the need of importing every single module from it.

Let's take, for example, the following package structure:

```commandline
Project
|-> math_figures\
    |    |-> __init__.py
    |    |-> circle.py
    |    |-> square.py
    |    |-> triangle.py
```

Without the help of `__init__.py`, the following is one possibility of how the imports would look:

```python
from math_figures.circle import Circle
from math_figures.square import Square
from math_figures.triangle import Triangle

if __name__ == "__main__":
    my_circle = Circle(...)
    my_square = Square(...)
    my_triangle = Triangle(...)
```

The first help that `__init__.py` provides us (even if we do not code anything within it) is to be able to import the whole package.
This cleans a lot of the imports:

```python
import math_figures

if __name__ == "__main__":
    my_circle = math_figures.circle.Circle(...)
    my_square = math_figures.square.Square(...)
    my_triangle = math_figures.triangle.Triangle(...)
```

However, this solution is still not the best one, as very long paths are required every time we decide to create a new instance from those classes.

The **best solution** is to move these long-path imports into the `__init__.py` module.

```python
# This is the __init__.py module
from math_figures.circle import Circle
from math_figures.square import Square
from math_figures.triangle import Triangle

__all__ = ["Circle", "Square", "Triangle"]
```

With those imports coded there, now all the classes can be directly imported into any other file from the module level:

```python
# Case 1: importing all the classes at the top level
from math_figures import Circle, Square, Triangle

# Case 2: importing the module only
import math_figures

my_circle = math_figures.Circle(...)
my_square = math_figures.Square(...)
my_triangle = math_figures.Triangle(...)
```

❗Please remember:<br>
Easy imports are to be used **from the outside of a package**.
If you start using them also from within, nothing will stop you, but you may come to the situation in which your code will not compile due to circular imports.
