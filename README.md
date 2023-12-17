# installable-library-python-test
a test of simple library for python to be pip installed 


path:

mylibrary/
│
├── mylibrary/
│   ├── __init__.py
│   └── hello.py
│
└── setup.py


mkdir mylibrary
touch mylibrary/__init__.py
touch mylibrary/hello.py
touch setup.py


git clone git@github.com-personal:michele1990/installable-library-python-test.git

pip install git+https://github.com/michele1990/installable-library-python-test.git
