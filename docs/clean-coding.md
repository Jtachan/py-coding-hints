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
* [Packages](#packages)
* [Sequences](#sequences)
  * [List and tuples](#lists-and-tuples)
  * [List comprehension](#list-comprehension)
  * [Generators](#generators)

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
- Provinding opertations on extra variables and the stored information.
- Creating a basic structure for multiple structures

**Classes** are to be named as the structure that the instance will hold.
Its **methods** follow the same naming conventions as the functions, as they are 'functions' that use information stored within the class.
Any **property** and **attribute** follow the variable's naming conventions, as they are 'variables' stored within the class.

Let's take a 'Circle' class as an example, that can hold attributes and properties:

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
print(my_circle.radius)  # This prints '3.5'
print(my_circle.diameter)  # This prints '7.0'
print(my_circle.area)  # This prints '21.991148575128552'
```

Note that the property `Circle.area` is actually a "function" that calculates the area of the circle.
However, due it is accessible as an attribute, it should not be named as an action, but as the value it returns.

## Packages

It is called a 'package' to some code that can be installed and imported for others to use in different python codes.
If you are already familiar with other programming languages, you might know them as 'libraries'.

An example of a very well-known and used package is [`numpy`](https://numpy.org/).
You can install it in your python environment by using the next command:

```commandline
pip install numpy
```

The installing command can also be modified to specify some release requirements:
* `pkg==X.Y.*`: This command will install the package version _'X.Y'_ with the latest _'Z'_ release version, updating it if called again.
* `pkg==X.Y.Z`, `pkg>=X.Y.Z`,`pkg<=X.Y.Z`: These commands work with the mentioned 'X.Y.Z' release. However, the use of these commands will not update any already installed package. The ">", ">=", "<" and "<=" can be included within the same line, just like `pkg>=X.Y.Z,<X+1` (install a version higher or equal to "X.Y.Z" but lower than "X+1.any.any")
* `pkg~=X.Y.Z`: Equivalent to `pkg>=X.Y.Z,<X.Y+1`. In other words, it will install an equal or higher version of "X.Y.Z" release but won't update.

To add the package to your code, this one has to be at the beginning of the file preceded by the keyword 'import'.
You can also add the keyword 'as' to import the package with a specific name.

```python
import numpy as np

angle_degrees = 60
angle_radians = np.deg2rad(angle_degrees)
```

## Sequences

### Lists and Tuples

**[Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)** are "arrays" of data, which can be modified by deleting items, adding new or modifying them.
Lists are defined with brackets `[]` containing all the items. 
The build-in function `list()` can also be called to transform a sequence into a list.

**Tuples** can be understood as lists that are not modifiable.
They are defined with parenthesis `()` containing all the items. 
There is also a build-in function `tuple()` to convert a sequence into a tuple.

In Python, it is possible to **iterate** over sequences without using any indexing:

```python
>>> numbers = (1, 2, 3)
>>> for n in numbers:
...    print(n)
1
2
3
```

### List comprehension

List comprehension allows creating lists with fewer lines of code.

Let's take the example we want to create a list with the letters of a word.
While we could iterate with a for-loop over the whole word to create the list (which is a valid solution),
a list comprehension would create the list in only one line of code:

````python
word = "python"

# No use of the list comprehension
letters = []
for letter in word:
    letters.append(letter)
print(letters)
# This prints ["p", "y", "t", "h", "o", "n"]

# Use of list comprehension
letters = [letter for letter in word]
print(letters)
# This prints ["p", "y", "t", "h", "o", "n"]
````

### Generators

While generators are not a sequence _per se_, we can think of them as one for iterating purposes.
It is very recommended to use them in applications to save memory for very large sets of information.

For example, we want to design a function that returns all lines in a text document.
Knowing everything explained in this section, this could easily be done creating a list:

````python
def listed_lines_in_document(file_path):
    with open(file_path) as file:
        all_lines = file.readlines()
    return all_lines
````

This function returns all lines of the document in a sequence.
While the purpose is fulfilled, very large documents will be inconvenient in the used memory.

A **generator** will return all lines one by one, without storing them anywhere.
This means once we iterate over the next item, the previous one is lost.
Generators can be defined in functions by using `yield` instead of return.

```python
def listed_lines_in_document(file_path):
    with open(file_path) as file:
        for line in file.readlines():
          yield line
```

If it is still hard for you to understand generators, comparing them to functions is a good way to understand them better:

| Functions                                  | Generators                                                |
|--------------------------------------------|-----------------------------------------------------------|
| Use the keyword `return`                   | Use the keyword `yield`                                   |
| The code stops after one value is returned | The code stops when it reaches the end of the coded logic |

At last, generators can also be defined similar to the list comprehension.
The stored in memory value will be a function that will iterate over some items:

```python
>>> numbers = (n for n in range(3))
>>> print(numbers)
<generator object <genexpr> at 0x000002F92972DD20>

>>> for number in numbers:
...    print(number)
1
2
3
```

Remember the functions `list()` and `tuple()` can be used to convert the object into a sequence.
This I find helpful for debugging purposes.
