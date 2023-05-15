# Python Basics

In this section, you can find some hits and rules, which could be used anywhere in python.


* [Naming](#naming)
* [Math and numbers](#math-and-numbers)
  * [Float numbers](#float-numbers)
  * [Cleaner numbers](#writing-clearer-numbers-for-coders)
* [Sequences in Python](#sequences-in-python)
  * [List and tuples](#lists-and-tuples)
  * [List comprehension](#list-comprehension)
  * [Generators](#generators)
* [Docstrings and type hints](#docstrings-and-type-hints)
* [Packages](#packages)

## Naming

While the general naming conventions to follow are the ones specified at the [Google styleguide](https://google.github.io/styleguide/pyguide.html#s3.16-naming), there are a few additions which don't break the convention and improve the code readability and maintenance:

1. **Do not shorten names**: While very long names are to be avoided, it is very helpful to use names like `vector_state` instead of `vec_st` or `lines_in_file` instead of `lf`. These short names might look understandable enough for you (the main developer), but not for the next one that works under the same code. There are very few exceptions (mainly for prefixes), like the use of `nof_` for `number_of_`.
2. **Use meaningful names**: This applies to everything. For example, after an operation do not use `res` nor `result`, because it does not show what the variable is holding. However, `predicted_speed` shows a very clear understanding of what it holds without looking further into the code.
3. **Function and methods names**: They should be named after the operation they pretend to work on. It is expected that the function `serialize_numpy_for_json(numpy_element)` will check the given element and transform it into Json serializable, due numpy elements are not serializable into Json without any modification.
4. **Variables and properties**: They should be named after the value they return. While this is clear for a variable, a class property might perform some operation before returning the result, do not be confused by it. E.G.: The class `Circle` should not contain the property `Circle.calculate_area`, but instead the `Circle.area` or even the method `Circle.calculate_area()`.

## Math and numbers

### Float numbers

Float numbers are those that contain decimals.
While this is a basic idea, it is crucial to understand all the characteristics that come into them.

When working with floats:
* Any mathematical operation containing floats will return always a float.
* They can be converted to integers by using `int()`. If so, the truncated value is returned.
* Two floats can never be directly compared by `==`

The third point needs a little bit of explanation.
Due to how Python handles floats, it is never a good idea to compare two of them with `==` to see if they are equal.
Instead, you should compare if **the difference** is lower than a defined threshold.

```python
# This is correct for comparing integers
>>> a, b, c = 1, 2, 3
>>> print(a + b == c)
True

# This is incorrect for comparing floats
>>> a, b, c = 0.1, 0.2, 0.3
>>> print(a + b == c)
False
# We can check what is being calculated as the sum of 0.1 and 0.2
>>> print(a + b)
0.30000000000000004

# This is correct for comparing floats
>>> a, b, c = 0.1, 0.2, 0.3
>>> print(abs(a + b - c) < 1e-6)
True
```

### Writing clearer numbers for coders

When coding numbers, sometimes large values are required.
Let's take, for example, we want to use `1000` instead of `1e3`.
In theory, they are both the same value, but in practise `1000` is type `int` while `1e3` is type `float`, so they are different for Python.

When coding a clean code, numbers can also be set with underscore "_".
This can be used to separate the numbers in pairs or like a point (european point on numbers).
That allows achieving behaviours like the next code:

```commandline
>>> number1 = 1000
>>> number2 = 1_000
>>> print(number1 == number2)
True
>>> number3 = 10_00
>>> print(number2 == number3)
True
```

The use of the underscore for the number "1000" is a little overkill, but it's exceptional to see the example.
<br/>I recommend integrating this behavior in your code for numbers with 5 digits or more.

## Sequences in Python

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

## Docstrings and type-hints

Any package needs to be supported and modify from time to time. It is crucial to create a code that can be easily understood. For it, docstrings and type hints help, then they are always a must at any quality code.

**Docstrings** contain the description and meaning of the function, as well as for the parameters and return value. I believe [numpy docstring](https://numpydoc.readthedocs.io/en/latest/format.html) is one of the clearest to use at any place.

**Type hints** show the type of the variable to be used within the parameters or to be returned. These do not only allow better understanding of the parameters, but also help to check correct variables are being given. Many of the simple types can be writen by their naming, as for example `str`, but others need of an extra library, as `List` from `typing` or `NDARRAY` from `numpy.typing`.


```python
from typing import Sequence

def count_total_lines(files_paths: Sequence[str]) -> int:
    """
    Count the total number of lines from several files.
    
    Parameters
    ----------
    files_paths: sequence of str
        Paths to the files to be read.
        
    Returns
    -------
    nof_lines: int
        Value of all lines from all the files together.
    """
    nof_lines = 0

    for file_path in files_paths:
        with open(file_path, "r") as file:
            nof_lines += len(file.readlines())

    return nof_lines
```

❗**Please note**
</br>While specifying the name of a variable and its type within both the function definition and the docstring might seem redundant, it is not that much.
Whenever the function `help()` is called over a function, this will return the docstring, while the type hints will help you to avoid errors by your IDE warnings.

Working like this will also help you to create sturdier codes. There might be cases in which it is clearer what type must be used after writing the description in the docstring.

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
