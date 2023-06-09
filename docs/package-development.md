# Packages in python

The word "Packages" defines every file and module that contains a set of files and folders for a python tool to run. This is defined as "Libraries" in other languages like C.

In this document, you will understand the basics about the parts of a package and how to work with it. You will also find links to other sections and files.

## Project structure

As just mentioned, the file that makes our package installable is the `setup.py`. However, keeping a good structure is crucial for our code to be easily maintainable.
While there is no rule about this structure for Python, I recommend using the following structure

```
Project
    |-> package_name\
    |    |-> __init__.py
    |    |-> main_file.py
    |    |-> folder_module_A
    |    |     |-> file_A.py
    |    |     |-> file_B.py
    |-> setup.py
    |-> Readme.md
    |-> examples\
    |-> unittests\
    |-> lint files
```

Here I provide you some descriptions about the folders and files shown in the structure.
Any further information is provided later on.

### Setup.py file

This is the main file making the package installable. 
There, the name to be used to install the package is specified.

To fully learn how to create your own `setup.py` file, you can read the [original documentation](https://docs.python.org/3/distutils/setupscript.html#writing-the-setup-script).
You can also make use of the [template setup file](../helpful_files/setup_template.py) I provide in this repository, at the "helpful_files" folder.

### Package folder

The folder `package_name` is to be named as the one to be imported in any python code. This one does not have to be the same as the one defined in the `setup.py`, although it is recommended for it to be similar at least.

For example, `numpy` uses the same name to install the package as well as to import it. However, `OpenCV` uses different names.

```commandline
pip install numpy
pip install opencv-python
```

```python
import numpy as np
import cv2
```

You can also see this folder contains a `__init__.py` file. 
This makes the package importable, as well as allows to make easy imports from the package.
Whenever you install the package, this folder is the one copied into the environment in which it is installed.

Within the folder, all the modules that compose the code are to be stored.
The rules and recommendations about these modules are explained further on in this document.

### Readme file

It might not look at it, but it is **extremely important** that your package is well documented so others can make use of it.
Do never assume that it is understood what your code does or which function is to be called at each moment.
It sounds exhausting, but there is nothing more exhausting than coming back to your old code, just to understand nothing and find no documentation whatsoever.

The `Readme.md` file is not the only type of documentation your code must have, but this file is as important (if not even more) than the code itself.

### Unit test folder

Any code may have bugs. While your current state might be totally free of bugs and stable, adding one single small new feature might break your tool somewhere unknown.

That is the reason to always have unit-tests. These tests must check:
* The code runs without errors
* Any important error to be raised is raised as it should
* The calculated values from the code are correct

If your unit test is good, whenever you introduce a new feature, the test code will tell you if everything is still correct or either the package or the testing code has to be updated.
Unit tests python packages are `pytest` and `unittest`. 
While both have their advantages and inconvenient, `pytest` is a more efficient tool for unit tests definitions.

Here you can learn more about [unit testing](unit-testing.md).

### Examples folder

While sometimes a quick example code in the `Readme.md` file might be enough, example codes are very helpful to understand and use the tool (depending on its usage).
Do not be afraid to write these, even if they are 4 lines of code, as they fulfill two main purposes:
- Showing people how the package is used
- Having small scripts that are easily modifiable to work with the tool

### Linting files

Lint files are always a very helpful resource to keep your code clean.
While there are different ones, I always prefer to work with two simultaneously, so my code is always doubled checked: [`Pylint`](https://pypi.org/project/pylint/) and [`Flake8`](https://flake8.pycqa.org/en/latest/). I also like to use the formatters [`isort`](https://pycqa.github.io/isort/) and [`black`](https://black.readthedocs.io/en/stable/).

Lints and formatters are very helpful tools that provide solutions for:
* Maintaining a well-structured code
* Finding errors within the code
* Helping you to reach and maintain a more consistent and sturdier code

While these tools might be almost "plug-and-play" solutions, I recommend you find a set of rules to maintain your code.
These rules have to be specified within these linting configuration files.
For example, `pylint` will check your code with the rules specified at the `pylintrc` file.
If this one is non-existing, then a default set of rules are used.

## Pipeline for development

Whenever you are working on a project, it is most possible that you encounter one or multiple of the following:
* There are multiple people working on the project on different tasks at the same repo
* You want to implement different unrelated features/fixes at the same time
* There is a need to track back when a change was made

Working on an online repo is a good solution for a whole team to work on the same tool at the same time without stepping on each other.
There are many different alternatives, like `Github` or `Gitea`.
<Br>Whenever you have decided which one to use, following the next bullet points will make everything easier in the future, for working with the previous enumerated situations:
1. **Keep a `master` and a `develop` branch protected**:<br>
The `master` branch should contain only the code that is stable and released. From it, the `develop` branch should contain any bugfix and new feature that has been reviewed. Protect always the branches so people cannot push on them directly, allowing them to contribute only with pull requests.
2. **Use correct namings on the branches**:<br>
Any new branch to modify the tool should be created up from the latest `develop`. Then, they can be named using prefixes to create organized folders. Although there are no established rules on this, these are the ones I recommend using:
  
    | Name                | Created from | Includes                                                                     | To be merged into |
    |---------------------|--------------|------------------------------------------------------------------------------|-------------------|
    | `feature\{NAME}`    | `develop`    | New functionalities for the tool                                             | `develop`         |
    | `bugfix\{NAME}`     | `develop`    | Fixes related to the code, which can wait until the next release of the tool | `develop`         |
    | `hotfix\vX.Y.{Z+1}` | `master`     | Fixes related to the code that compromise the stability of the tool          | `master`          |
    | `release\vX.Y.Z`    | `develop`    | All reviewed changes that create the new code release                        | `master`          |
3. **Create clear commits**:<br>
Many people make commits like `corrected issue`. While this is a very valid commit, it will create a very tough situation when tracking back a specific change. I recommend making multiple commits, separating that only commit into:
   - C1: `renamed function parameter`
   - C2: `introduced new dataclass to hold the intermediate state`
   - C3: `corrected the math contained at the prediction's calculation`
4. **Make sure all additions are reviewed**:<br>
It might sound like a very basic concept, but it is very necessary. Sometimes, the new additions create new bugs that can be fixed before merging it into the code, or even the code itself can be optimized. Having someone else review your code will always help on finding these situations and merging a better code (as long as the reviewer takes the task seriously).

As you can see, the steps to follow are not complicated at all.
Feel free to update this to the routine that works better for you, but don't forget to plan ahead to avoid creating more problems for your future self.

## Modules

When creating packages, it is very common to create multiple modules (python files) containing different codes.
This is a very extended routine, as it is also a good solution to organize the code.
However, to avoid everything to be disorganized, it is important to keep in mind:
* How to separate the modules
* How to name the modules

As a good practice to keep everything tidy up, these are the key points I recommend:

- Module's names should be in `snake_case` in reference to what they contain.
- Any new class that potentially can be used in multiple places should be stored at its own module.
- Any class/function used only in one module (and not available to the user) doesn't need an extra module.
- Command line interface scripts can be stored at:
  - The module with the main functionality
  - A new module named `_cli_scripts.py` or similar (preferred)

Each module should start with a docstring, specifying what the module contains as a general description.

```python
# File math_shapes/circle
"""
This module contains the class Circle
"""
import numpy as np


class Circle:
    """
    Class to represent the mathematical shape of a circle and its properties.
    """
    ...
```

## Implementing easy imports

As you can notice at the [specified package structure](#project-structure), all Python packages contain a `__init__.py`.
This file makes the package importable and does not really need to be filled for the package to work; however, I can strongly recommend filling it.

To understand "easy importing", let's work with an example here; let's suppose the following package:
```
math_shapes\
    |-> __init__.py
    |-> circle.py
    |-> square.py
```

Now, the following is an example code on a script using both classes defined within the package:

```python
from math_shapes.circle import Circle
from math_shapes.square import Square

my_circle = Circle(radius=3)
my_square = Square(length=2)
```

While the code will work properly, it is not the most efficient package to use, as the classes have to be imported from each different module.
Here is where the `__init__.py` shines and makes everything easier for the user:

```python
"""This is the __init__.py file"""
from math_shapes.circle import Circle
from math_shapes.square import Square
__all__ = ["Circle", "Square"]
```

Containing this init file, now the whole module can be imported and classes can be used directly from it:

```python
import math_shapes as shapes

my_circle = shapes.Circle(radius=3)
my_square = shapes.Square(length=2)
```

Remember to add to the `__init__.py` file all that is designed to be reachable for the user.

## Releasing

There will reach the point in which we want to release the package we've been working on. It does not matter if it is a pre-release, a first release or any other possibility. 

Releasing a package means increasing the version number `X.Y.Z` specified at the `setup.py` file (as long as you decide to use [semantic versioning](https://semver.org/)). The `X.Y.Z` refer to the `Mayor.Minor.Patch` numbers.

**When to increase each number**:

- `Patch`: If a hotfix is implemented or the latest `develop` to merge contains only bugfixes.
- `Minor`: If the tool contains new functionalities, and it is still backwards compatible with the previous releases that share the same major release. The `Patch` number has to be reset to 0, even in the new release contains bugfixes.
- `Major`: If there is **any change** at the tool that makes it incompatible with the latest previous release. These can be renaming functions/classes/variables/parameters, deprecating old functionalities that the user can call, renaming the files and modules, etc. Both `Minor` and `Patch` numbers must be reset to 0.
