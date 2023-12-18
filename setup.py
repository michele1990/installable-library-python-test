from setuptools import setup, find_packages
import os

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    description='A simple print function',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/michele1990/installable-library-python-test.git',
    install_requires=[
        # Dependencies here, e.g., 'requests'
    ],
)
