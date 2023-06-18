isort pymath_tools setup.py unittests PROJECT_PKG_FOLDER
black pymath_tools setup.py unittests
pip install .
flake8 --tee --format=pylint unittests PROJECT_PKG_FOLDER
pylint --rcfile=pylintrc PROJECT_PKG_FOLDER
pylint --rcfile=pylintrc unittests --recursive=y
