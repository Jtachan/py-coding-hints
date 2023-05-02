# Packages in python

The word "Packages" defines every file and module that contains a set of files and folders, for a python tool to run. This is defined as "Libraries" in other languages like C.

In this document, you will understand the basics about the parts of a package and how to work with it. You will also find links to other sections and files.

**Table of contents**
* [Installation](#installation)
* [Project structure](#project-structure)
  * [Setup file](#setuppy-file)
  * [Package folder](#package-folder)
  * [Readme](#readme-file)
  * [Unit test](#unit-test-folder)
  * [Examples](#examples-folder)
  * [Linting](#linting-files)
* [Pipeline of development](#pipeline-of-development)

## Installation

Whenever a user decides to install a package, this can be done via `pip` commands. Let's take numpy as an example:

```commandline
pip install numpy
```

There are cases in which we decide to create our own package. In these cases, a `setup.py` file is required. This file is what makes our code installable and importable, just like we could do with others like `numpy`. To install any local changes, the command to use is the following:

```commandline
pip install .
```

## Project structure

As just mentioned, the file that makes our package installable is the `setup.py`. However, keeping a good structure is crucial for our code to be easily maintainable.
While there is no rule about this structure for Python, I recommend to use the following structure

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
Any further on information is provided later on.

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

If your unit-test is good, whenever you introduce a new feature the test code will tell you if everything is still correct or either the package or the testing code have to be updated.

### Examples folder

While sometimes a quick example code in the `Readme.md` file might be enough, example codes are very helpful to understand and use the tool (depending on its usage).
Do not be afraid to write these, even if they are 4 lines of code, as they fulfill two main purposes:
- Showing people how the package is used
- Having small scripts that are easily modifiable to work with the tool

### Linting files

Lint files are always a very helpful resource to keep your code clean.
While there are different ones, I always prefer to work with two simultaneously, so my code is always doubled checked: [Pylint](https://pypi.org/project/pylint/) and [Flake8](https://flake8.pycqa.org/en/latest/).

## Pipeline of development
