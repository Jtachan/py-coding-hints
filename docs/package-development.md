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
While there are different ones, I always prefer to work with two simultaneously, so my code is always doubled checked: [`Pylint`](https://pypi.org/project/pylint/) and [`Flake8`](https://flake8.pycqa.org/en/latest/). I also like to use the formatters [`isort`](https://pycqa.github.io/isort/) and [`black`](https://black.readthedocs.io/en/stable/).

Lints and formatters are very helpful tools that provide solutions for:
* Maintaining a well-structured code
* Finding errors within the code
* Helping you to reach and maintain a more consistent and sturdier code

While these tools might be almost "plug-and-play" solutions, I recommend you find a set of rules to maintain your code.
These rules have to be specified within these linting configuration files.
For example, `pylint` will check your code with the rules specified at the `pylintrc` file.
If this one is non-existing, then a default set of rules are used.

## Pipeline of development

Whenever you are working on a project, it is most possible that you encounter one or multiple of the following:
* There are multiple people working on the project on different tasks at the same repo
* You want to implement different unrelated features/fixes at the same time
* There is a need to track back when a change was made

Working on an online repo is a good solution for a whole team to work on the same tool at the same time without stepping on each other.
There are many different alternatives, like `Github` or `Gitea`.
<br>Whenever you have decided which one to use, following the next bullet points will make everything easier in the future, for working with the previous enumerated situations:
1. **Keep a `master` and a `develop` branch protected**:<br>
The `master` branch should contain only the code that is stable and released. From it, the `develop` branch should contain any bugfix and new feature that has been reviewed. Protect always the branches so people cannot push on them directly, allowing them to contribute only with pull requests.
2. **Use correct namings on the branches**:<br>
Any new branch to modify the tool should be created up from the latest `develop`. Then, they can be named using prefixes to create organized folders. Although there is no established rules on this, these are the ones I recommend to use:
  
    | Name                | Created from | Includes                                                                     | To be merged into |
    |---------------------|--------------|------------------------------------------------------------------------------|-------------------|
    | `feature\{NAME}`    | `develop`    | New functionalities for the tool                                             | `develop`         |
    | `bugfix\{NAME}`     | `develop`    | Fixes related to the code, which can wait until the next release of the tool | `develop`         |
    | `hotfix\vX.Y.{Z+1}` | `master`     | Fixes related to the code that compromise the stability of the tool          | `master`          |
    | `release\vX.Y.Z`    | `develop`    | All reviewed changes that create the new code release                        | `master`          |
3. **Create clear commits**:<br>
Many people make commits like `corrected issue`. While this is a very valid commit, it will create a very tough situation when tracking back a specific change. I recommend to make multiple commits, separating that only commit into:
   - C1: `renamed function parameter`
   - C2: `introduced new dataclass to hold the intermediate state`
   - C3: `corrected the math contained at the prediction's calculation`
4. **Make sure all additions are reviewed**:<br>
It might sound like a very basic concept, but it is a very necessary one. Sometimes, the new additions create new bugs that can be fixed before merging it into the code, or even the code itself can be optimized. Having someone else review your code will always help on finding these situations and merging a better code (as long as the reviewer takes the task seriously).

As you can see, the steps to follow are not complicated at all.
Feel free to update this to the routine that works better for you, but don't forget to plan ahead to avoid creating more problems for your future self.
