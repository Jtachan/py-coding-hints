# Packages in python

The word "Packages" defines every file and module that contains a set of files and folders, for a python tool to run. This is defined as "Libraries" in other languages like C.

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


