"""
Fill all the specified fields. Extend other fields if you think it could be
required.
"""
import setuptools

package_url = "https://github.com/Jtachan/py-coding-hints.git"

setuptools.setup(
    name="python-coding-hints",
    url=package_url,
    description="This repository is pure for learning purposes",
    author="Jaime Gonzalez Gomez",
    author_email="jaimenicolas.gonzalezg@gmail.com",
    version="0.0.0",
    install_requires=[
        "numpy>=1.20.0",
    ],
)
