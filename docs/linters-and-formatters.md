# Linters and formatters

When writing a code, there are two main points to have in consideration:
- Maintain the code quality
- Maintain a good and consistent structure

Linters will help with the first point, while formatters will help with the second one.

Both are external python packages, which you will need to install in your environment for them to work.
However, take in consideration they are not requirements for your project, but for any developer to work on it.
For it, you should always keep a **separate requirements file**.

Within [`helpful_files\dev_requirements.txt`](../helpful_files/dev_requirements.txt) you can find the file I like to have for these cases.
Feel free to add it into your project and run the next command to install them.

```commandline
pip install -r dev_requirements.txt
```

From this point on, the document will assume you have installed all of them.
Also, 

## Formatters
Formatters are codes to run to always keep your code within under some style rules.
These rules, for example, can specify the line length or how to format long in-brackets statements.

The following formatters do not require any configuration file, thus they are mostly configured with commands whenever they are called.

### Black

[`black`](https://black.readthedocs.io/en/stable/index.html) will check mainly for a correct line length, not exceeding the specified limit (88 character-line-length by default).
If any line exceeds it, the program will automatically reformat it into multiple lines.
You can also specify another line length:

```commandline
black --line-length 120 folder_path
```

If instead you give the `--check` command, the files will not be reformatted.
Instead, it will print if all files are ok or some should be reformatted.
This is actually pretty neat to put as a check state for your repo, to be done every time new changes are pushed:
```commandline
black --check file.py
```

Check the documentation, as it is capable of more.
<br>https://black.readthedocs.io/en/stable/index.html

### isort

[`isort`](https://pycqa.github.io/isort/) takes the name from "imports sorting".
Its main functionality, as you can guess, is to sort the imports from the specified file or from all the files within one specified folder.
```commandline
isort folder_path
```

Just like `black`, it also has the line length and the check commands.

Check the documentation, as it is capable of more.
<br>https://pycqa.github.io/isort/

## Linters

Linters will check your code structure and will warn you whenever there are inconsistencies.

For example, let's suppose you want to add a try/except for checking if a key is within a dictionary:

```python
try:
    value = my_dict[key]
    value += 1/0
except:
    print(f"'{key}' is not in the dictionary")
```

Your linters will complain here, as using only 'except' is a very broad case.
In other words, that 'except' statement will catch any error and run the 'print'.

If you have experience in python, you will know the problem here:
The dictionary might have the given key, but python will raise `ZeroDivisionError` and the 'except' block will catch it.
Instead, that line should be `except KeyError`.

This is but only one example of why linters will help you find inconsistencies in your code.

### flake8

[`flake8`](https://flake8.pycqa.org/en/latest/) is a rapid-run linter.
Just as `black` and `isort`, it doesn't need any configuration file and everything is configured by commands.

Its default profile runs for 80 character-line-length.
```commandline
flake8 file.py
```

### pylint

[`pylint`](https://pylint.readthedocs.io/en/latest/user_guide/usage/run.html) will check within your code for very specific rules, like namings, maximum parameters in a function/method or maximum lines within a module, among many others.

For it, this will take a configuration file (usually named `pylintrc`) in where everything is defined.
You can find a template of it within [`helpful_files\pylintrc`](../helpful_files/pylintrc).
If you have one, you'll need to specify where it lays with the command `--rcfile`.
Otherwise, it will take a default in-build to pylint configuration.

```commandline
pylint --rcfile=pylintrc file.py
```

One very cool feature I believe it has for beginners is that it will return you a score on your own code, which will push you to always improve your code quality.


## Profiling (tox)

[`tox`](https://tox.wiki/en/latest/index.html) was created with the idea of having only one profile configuration file, instead of many different.
Using tox has many advantages:
- Solving conflicts among the formatters/linters within your project.
- Profiling to run the unittests in multiple python versions.
- Automatic profiling for checks within the project.

To fully understand it, I'll be explaining the configuration within [`helpful_files\tox.ini`](../helpful_files/tox.ini).
This file should be contained within the top level of your project and will make sure all previous advantages are correct.
Let's go one by one with them:

**Solving formatters' conflicts**

The first lines you would encounter in the `tox.ini` linked file are these:

````yaml
[flake8]
max-line-length = 88

[isort]
profile = black
````

These are two profiles, regarding a linter (`flake8`) and a formatter (`isort`).
Without these profiles, the first thing you would encounter (if you try to run all the linters and formatters at once) are the following problems:
* `isort` and `black` will always reformat your files, as they have different base profiles configuration.
* After the `black` reformat (line length = 88 characters by default), `flake8` might complain you have many lines which are longer than 80 characters (if you are still using the default configuration)

However, with the profiles specified in `tox.ini` these won't happen.
Within the file, each block starting as `[NAME]` is a profile.
Each profile then establishes its own configuration before running any commands.

Then, whenever you run `isort`, `tox` will first look if this command has a profile within the file. 
If so, it will then configure anything written there and then run the command.

Due to this behavior, all three `isort`, `black` and `flake8` will have the same line length, and you won't have any check conflict.

**Automatic unittests**

The profiles also work with `tox` itself.
For it, let's take it step by step.

The following is the profile for `tox`:
```yaml
[tox]
envlist = py{38, 39, 310, 311}
requires = virtualenv>=20.0
```

This means that, whenever you call `tox`, it will create 4 virtual environments: the python versions from 3.8 to 3.11.
For this, tox will make sure (before any environment is created) that the package `virtualenv` is installed at the version 20.0 or higher.

Then, each environment will run the following profile:
```yaml
[testenv]
description = run unit test
deps = 
    numpy>=1.20.0
    pytest==7.3.*
commands = pytest unittests
```

Here we encounter:
* `description`: As its name indicates, this is just a description about what the profile will do. In this case, it will run the unit tests.
* `deps`: These are all the dependencies needed for the profile. It looks like it requires numpy and pytest to work. Remember to add here your project too as "." (current directory) if this one is a package.
* `commands`: As the name describes, these are te commands to run. This profile will run only one command: pytest on the "unittests" folder.

Once everything is set up, all you need is to run the following command:
```commandline
tox
```

Please have in mind 4 different environments will be created, each one installing the dependencies, and will run some commands.
It might take a while until all the files are run, so this should be done mostly when you are sure all your development has ended, and you want to push your changes.

**Automatic checks**

So now we know that `tox` allows to create multiple profiles to perform tasks.
That is good. However, we still need to run all checks on our code as fast as possible.

While we could add the dependencies and commands to our previous `[testenv]` profile, this is a solution to fully ignore for two reasons:
1. It will make the run even longer, as now there are more dependencies to install and commands to run.
2. The checks will be done 4 times, one per environment (that is overkill).

Instead, a new environment with another name can be created under `[tox]`. This one will be called "linters":
```yaml
[tox]
envlist = py{38, 39, 310, 311}, linters
```

Now "linters" is a new profile, totally separated from the others.
That means it also requires its own profile rules:

````yaml
[testenv:linters]
description = check code style
basepython = python3.8
deps =
    flake8==6.0.*
    pylint==2.17.*
    black==23.3.*
    isort==5.12.*
commands =
    isort --check unittests folder_name
    black --check unittests folder_name
    flake8 --tee --format=pylint unittests folder_name
    pylint --rcfile=pylintrc unittests folder_name
````

So as you can tell, the profile block is just named as `[testenv:PROF_NAME]`.
Within this profile, there is a new field named `basepython`.
This one is needed because now it is unknown to `tox` which python's version should run.
In this case, it is now configured at python 3.8.

Then, that solves the problem and whenever we run `tox` five environments will be installed: 4 for the tests and 1 for checking the code.

There is one more functionality: to run only one specific profile.
Let's suppose now we want to check the code within the project but not running the tests.
Then, we just have to use the following command:

```commandline
tox -e linters
```

This will run only the "linters" profile.
I do not advise doing this to run all the linters, as it will create a new temporary environment only for that, and it will always be faster to run the commands in the working virtual environment.

You can also create a `.bat` file (for Windows) to call it and run sequentially these commands.
This is what I usually do, and I provide you this file at `helpful_files\check_code.bat`, which you can open with a text editor and modify if needed.
To run it, you just need to give its path in the command line interface.

Now you know the basics about `tox`.
I encourage you to look at their documentation to find even more features:
<br>https://tox.wiki/en/latest/user_guide.html
