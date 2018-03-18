import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "kPyWavelet",
    version = "0.0.1",
    author = "Sebastian Krieger,Eduardo dos Santos Pereira",
    author_email = "sebastian@nublia.com,pereira.somoza@gmail.com",
    description = ("Tools For Wavelet Analises in Python"),
    license = "BSD",
    keywords = "wavelet signal analises ",
    url = "https://github.com/duducosmos/kPyWavelet",
    packages=['kPyWavelet','kPyWavelet/sample'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
