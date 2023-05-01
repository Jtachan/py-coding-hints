# Python Clean Coding Hints

At this section you can find some hits and rules, which could be used anywhere at python.

* [Naming](#naming)
* [Numbers](#numbers)
* [Docstrings and type hints](#docstrings-and-type-hints)
* [Imports](#imports)

## Naming

While the general naming conventions to follow are the ones specified at the [Google styleguide](https://google.github.io/styleguide/pyguide.html#s3.16-naming), there are a few additions which don't break the convention and improves the code readability and maintenance:

1. **Do not shorten names**: While very long names are to be avoided, it is very helpful to use names like `vector_state` instead of `vec_st` or `lines_in_file` instead of `lf`. These short names might look understandable enough for you (the main developer), but not for the next one that works under the same code. There are very few exceptions (mainly for prefixes), like the use of `nof_` for `number_of_`.
2. **Use meaningful names**: This applies for everything. For example, after an operation do not use `res` nor `result`, because it does not show what the variable is holding. However, `predicted_speed` shows a very clear understanding of what it holds without looking further into the code.
3. **Function and methods names**: They should be named after the operation they pretend to work on. It is expected that the function `serialize_numpy_for_json(numpy_element)` will check the given element and transform it into a Json serializable, due numpy elements are not serializable into Json without any modification.
4. **Variables and properties**: They should be named after the value they return. While this is clear for a variable, a class property might perform some operation before returning the result, do not be confused by it. E.G.: The class `Circle` should not contain the property `Circle.calculate_area`, but instead the `Circle.area` or even the method `Circle.calculate_area()`.

## Numbers

When coding numbers, sometimes large values are required.
Let's take, for example, we want to use `1000` instead of `1e3`.
In theory, they are both the same value, but in practise `1000` is type `int` while `1e3` is type `float`, so they are different for Python.

When coding a clean code, numbers can also be set with underscore "_".
This can be used to separate the numbers in pairs or like a point (european point on numbers).
That allows to achieve behaviours like the next code:

```commandline
>>> number1 = 1000
>>> number2 = 1_000
>>> print(number1 == number2)
True
>>> number3 = 10_00
>>> print(number2 == number3)
True
```

The use of the underscore for the number "1000" is a little overkill, but it's very good to see the example.
<br/>I recommend to integrate this behaviour in your code for numbers with 5 digits or more.

## Docstrings and type-hints

Any package needs to be supported and modify from time to time. It is crucial to create a code that can be easily understood. For it, docstrings and type hints help, then they are always a must at any quality code.

**Docstring** contain the description and meaning of the function, as well as for the parameters and return value. I believe [numpy docstring](https://numpydoc.readthedocs.io/en/latest/format.html) are one of the clearest to use at any place.

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

## Imports

Regarding imports, there are two main topics to always remember:
- What is being imported
- Should an alias be used

Whenever importing, it is highly recommended to import the package instead of the function to use.
</br>**Example**: We want to use the function from numpy to convert numbers from degrees to radians. If we are running a very small script just for testing, the next might seem logical:

````python
from numpy import deg2rad

radians = deg2rad(64.4)
print(radians)
# This will print "1.1239920382843482"
````

However, when creating any code is will come the time in which more functions are needed from the same package. Importing the whole package prevents to import all these functions one by one. 

Then, all imports are used as ``{package_name}.{function/class}``. This also improves the understanding of the code, showing clearly from which package comes the called function.

````python
import numpy

radians = numpy.deg2rad(64.4)
print(radians)
# This will print "1.1239920382843482"

array = numpy.array([radians])
````

This leads to the next issue: some modules contain inconvenient names to use, maybe because they are to complex to understand or a long path to call them.
For it, Python includes the use of alias, allowing to rename an import by using the keyword ``as``.
An alias is a very helpful tool to short anything, however keep in mind that a strange combination of letters can also make the code uglier or harder to understand.

```python
import numpy as np

radians = np.deg2rad(64.4)
print(radians)
# This will print "1.1239920382843482"
```

Do not be afraid of using alias. I recommend to use aliases within the next cases:
- To rename the import to a word clear to understand
- To rename the import into a maximum 3-character combination that relates to the package name, like ``import dataclasses as dtc``
