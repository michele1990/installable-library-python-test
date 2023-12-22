# installable-library-python-test
a test of simple library for python to be pip installed 

## Directory Structure

\'''
mylibrary/
│
├── mylibrary/
│   ├── __init__.py
│   └── hello.py
│
└── setup.py
\'''

## Setup Instructions

1. Create the directory and files:

   \'''bash
   mkdir mylibrary
   touch mylibrary/__init__.py
   touch mylibrary/hello.py
   touch setup.py
   \'''

2. Clone the repository:

   \'''bash
   git clone git@github.com-personal:michele1990/installable-library-python-test.git
   \'''

3. Install the library:

   \'''bash
   pip install git+https://github.com/michele1990/installable-library-python-test.git
   \'''
