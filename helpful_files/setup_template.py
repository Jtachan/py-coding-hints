"""
Make sure to adapt all the fields of this file to what your package requires.
Don't forget to rename this file to 'setup.py'
"""
import setuptools

repo_url = "https://github.com/Jtachan/py-coding-hints.git"

if __name__ == "__main__":
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        url=repo_url,
        name="python-coding-hints",
        author="XXX",
        author_email="XXX",
        version="0.0.0",
        python_requires=">=3.8",
        description="This repository is pure for learning purposes",
        long_description=long_description,
        long_description_content_type="text/markdown",
        install_requires=[
            "numpy>=1.20.0",
        ],
        entry_points={
            "console_scripts": [
                # ScriptName=path.to.module.py:function_name
            ]
        },
    )
