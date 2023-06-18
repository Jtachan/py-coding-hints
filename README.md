# Python Coding Guidelines

This repository is a guideline of some coding I've been learning. 
I like to think that I still can learn as much as possible, so this is a readme explaining (with examples) some python that improved my coding, and I hope can also help others.

The explanations given in all the following sections assume that **you know the basics of Python**.
If you are a Python newby, this repo will help you to get better, although it is not a tutorial.
If you are more advanced programming, I hope the explanations given make you even better coder.

It is no holy text, so don't take everything as a must, but as a recommendation for coding with Python following most of the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
If there is any modification that you might think it would improve this guide, anyone can open a pull request and ask me for the review.
This guide is organized in different folders, each one explaining the ideas of the topic.

## External useful pages

Here are also some online tools, which can help depending on the python script that you are working on:

| **Tool**                                                                   | **Description**                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------| 
| [Regex 101](https://regex101.com/)                                         | Creating and testing regex expressions for multiple languages | 
| [3D Rotation Converter](https://www.andre-gaschler.com/rotationconverter/) | Converting euler angles to rotation matrix or quaternions     |

## Table of content

* [**Python clean coding**](docs/clean-coding.md)
  * [Naming conventions](docs/clean-coding.md#naming-conventions)
    * [Variables](docs/clean-coding.md#variables)
    * [Functions](docs/clean-coding.md#functions)
    * [Classes](docs/clean-coding.md#classes)
  * [Documenting your project](docs/clean-coding.md#documenting-your-project)
    * [Type hints](docs/clean-coding.md#type-hints)
    * [Docstrings](docs/clean-coding.md#docstrings)
  * [Organizing your project](docs/clean-coding.md#organizing-your-project)
    * [Project's files](docs/clean-coding.md#projects-files)
    * [Easy imports](docs/clean-coding.md#easy-imports)
* [**Package development**](docs/package-development.md)
  * [Project structure](docs/package-development.md#project-structure)
    * [Setup file](docs/package-development.md#setuppy-file)
    * [Package folder](docs/package-development.md#package-folder)
    * [Readme](docs/package-development.md#readme-file)
    * [Unit tests folder](docs/package-development.md#unit-test-folder)
    * [Examples folder](docs/package-development.md#examples-folder)
    * [Linting](docs/package-development.md#linting-files)
  * [Pipeline for development](docs/package-development.md#pipeline-for-development)
  * [Modules](docs/package-development.md#modules)
  * [Implementing easy imports](docs/package-development.md#implementing-easy-imports)
  * [Releasing](docs/package-development.md#releasing)
* [**Formatters and linters**](docs/linters-and-formatters.md)
  * [Formatters](docs/linters-and-formatters.md#formatters)
    * [black](docs/linters-and-formatters.md#black)
    * [isort](docs/linters-and-formatters.md#isort)
  * [Linters](docs/linters-and-formatters.md#linters)
    * [flake8](docs/linters-and-formatters.md#flake8)
    * [pylint](docs/linters-and-formatters.md#pylint)
  * [Profiling (tox)](docs/linters-and-formatters.md#profiling-tox)
* [**Unit Testing**](docs/unit-testing.md)
  * [Pytest Vs Unittest](docs/unit-testing.md#pytest-vs-unittest)
  * [Essentials](docs/unit-testing.md#essentials)
  * [Pytest useful features](docs/unit-testing.md#pytest-useful-features)
