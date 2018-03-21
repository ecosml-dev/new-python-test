import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "new_python_test",
    version = "0.0.1",
    author = "jrmerz",
    description = ("this is a test, this is only a test!"),
    license = "MIT",
    keywords = "testing test test",
    url = "http://localhost:3000/package/3bd2f904-7b53-427c-99cd-6b65dc33a418",
    packages=[
        'new_python_test',
        'new_python_test.coefficients',
        'new_python_test.examples',
        'new_python_test.main'
    ],
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)